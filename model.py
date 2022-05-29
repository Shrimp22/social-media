from db import db

# User database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(50), nullable=False)
    comments = db.Column(db.JSON)

