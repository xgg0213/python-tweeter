from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Tweet(db.Model):
    __tablename__="tweets"

    id=db.Column(db.Integer, primary_key=True)
    tweet=db.Column(db.String(255))
    author=db.Column(db.String(255))
    date=db.Column(db.DateTime)
    likes=db.Column(db.Integer)
    