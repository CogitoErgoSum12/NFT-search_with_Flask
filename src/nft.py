import pandas

from src.base import db
from flask import Flask


class Nft(db.Model):
    nft_id = db.Column(db.Integer, primary_key=True)
    nft_name = db.Column(db.String, nullable=False)
    nft_image = db.Column(db.String, nullable=False)
    nft_address = db.Column(db.String, nullable=False)
    
    
    def addToDb(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def checkInDb(cls, nft_address):
        return cls.query.filter_by(nft_address = nft_address).first()

    






