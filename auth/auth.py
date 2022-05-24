from flask import Blueprint, jsonify, request
from db import db 
from model import User
from validate_email_address import validate_email
bp = Blueprint('auth',__name__,url_prefix="/usr")

# For update: Add bycrypt to make a hash password in register and into login to check hash passowrd

@bp.route('/register', methods=(["POST","GET"]))
def register():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    conf_password = request.json.get('conf_password')
    email_check = validate_email(email, verify=True)
    if password != conf_password:
        return jsonify(detail="Error! password need to be same"), 409

    if email_check == True:
        insert_query = User(username=username, email=email, password=password)
        db.session.add(insert_query)
        db.session.commit()
        return jsonify(detail="Register Sec welcome"), 200
    else:
        return jsonify(detail="Email not found"), 404


@bp.route('/login', methods=(["POST"]))
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    check_user = User.query.filter(User.username == username and User.password == password).first()

    if check_user:
        return jsonify(detail="Welcome"), 200
    else:
        return jsonify(detail="Error! User not found"), 404
