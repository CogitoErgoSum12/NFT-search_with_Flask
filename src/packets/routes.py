import requests

from flask import  render_template, request, redirect, make_response, flash, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_required, login_user, logout_user

from packets import app
from packets.models import Nft, Users


@app.route('/', methods=['GET'])
def nft_page():
    return render_template('nft_page.html')


@app.route('/nft_search', methods=['GET'])
@login_required
def nft_search():
    args = request.args['args']

    url = f"https://solana-gateway.moralis.io/nft/mainnet/{args}/metadata"

    headers = {

        "accept": "application/json",

        "X-API-Key": "S77RJTmiMoBbTQTEed5MExSDfHQ2HolnDEXy7GZRoo3Eah6t1YAR20dfdGIJASaT"

    }

    response = requests.get(url, headers=headers)

    nft = Nft()
    db_exist = nft.checkInDb(args)

    if db_exist:
        payload = db_exist
        return make_response(render_template('nft_result.html', payload=payload))

    response2 = response.json()

    payload = {

        "name": response2["name"],
        "description": response2["metaplex"]["metadataUri"],
        "address": response2["mint"]

    }

    nft = Nft(**payload)

    nft.addToDb()

    return make_response(render_template('nft_result.html', payload=payload))


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = Users.query.filter_by(login=login).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            next_page = request.args.get('next')

            return redirect(next_page)
        else:
            flash('Login or password is not correct.')
    #else:
    #    flash('Fill login and password.')

    return render_template('login.html ')


@app.route('/register', methods=['GET', 'POST'])
def register():
    login = request.form.get('login')
    password = request.form.get('password')
    password_retype = request.form.get('password_retype')


    existing_user_username = Users.checkInDb(login)


    if request.method == 'POST':
        if existing_user_username:
            flash('That username already exists. Please choose a different one.')    
        if not (login or password):
            flash('Not correctly filled')
        elif password != password_retype:
            flash('Passwords not equal')
        elif not existing_user_username:
            hash_password = generate_password_hash(password)
            payload_user = Users(login=login, password=hash_password)

            payload_user.addToDb()

            return redirect(url_for('login_page'))
    

    return render_template('register.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_page'))


# functions
@app.after_request
def redirectToNextPage(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)

    return response
