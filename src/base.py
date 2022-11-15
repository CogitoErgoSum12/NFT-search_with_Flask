from flask import Flask, render_template, request, redirect, url_for, make_response, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

from werkzeug.security import check_password_hash, generate_password_hash

import requests


app = Flask(__name__)
app.secret_key = '!@#$%^&*'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/python'
app.config['SQLALCHEMY TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

manager = LoginManager(app)
manager.login_view = 'login_page'

# functions

@app.errorhandler(404)
def page_not_found(e):
    render_template('404.html'), 404


@manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String,  nullable=False)
    password = db.Column(db.String,  nullable=False)

    def addToDb(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def checkInDb(cls, username):
        return cls.query.filter_by(login=username).first()



class Nft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    def addToDb(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def checkInDb(cls, nft_address):
        return cls.query.filter_by(address=nft_address).first()


with app.app_context():
    db.create_all()


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
    try:
        payload = {

            "name": response2["name"],
            "description": response2["metaplex"]["metadataUri"],
            "address": response2["mint"]

        }
    except KeyError:
        return make_response(render_template('404.html'))
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


@app.after_request
def redirectToNextPage(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)

    return response

if __name__ == "__main__":
    app.run(debug=True)
