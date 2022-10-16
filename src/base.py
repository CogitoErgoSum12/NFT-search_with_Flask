#!/usr/bin/env python3
import requests
from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/python'
app.config['SQLALCHEMY TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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
        return cls.query.filter_by(address = nft_address).first()


with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def nft_page():
    return render_template('nft_page.html')


@app.route('/nft_search', methods=['GET'])
def nft_search():
    args = request.args['args']
   
    url = f"https://solana-gateway.moralis.io/nft/mainnet/{args}/metadata"

    headers = {

        "accept": "application/json",

        "X-API-Key": "S77RJTmiMoBbTQTEed5MExSDfHQ2HolnDEXy7GZRoo3Eah6t1YAR20dfdGIJASaT"

    }

    response = requests.get(url, headers=headers)

    nft = Nft()                                     
    dbExist = nft.checkInDb(args)


    if dbExist:
        payload = dbExist
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

if __name__ == "__main__":
    app.run(debug=True)

