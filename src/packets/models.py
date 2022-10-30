
from flask_login import UserMixin

from packets import db, manager


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

