from flask import Blueprint, jsonify, request
from db import db 
from model import User
from validate_email_address import validate_email
from flask_bcrypt import Bcrypt

bc = Bcrypt() 
bp = Blueprint('auth',__name__,url_prefix="/usr")
# For update: Add bycrypt to make a hash password in register and into login to check hash passowrd

@bp.route('/register', methods=(["POST","GET"]))
def register():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    conf_password = request.json.get('conf_password')
    hash_pw = bc.generate_password_hash(password)
    email_check = validate_email(email, verify=True)
    if password != conf_password:
        return jsonify(detail="Error! password need to be same"), 409

    if email_check == True:
        insert_query = User(username=username, email=email, password=hash_pw)
        db.session.add(insert_query)
        db.session.commit()
        return jsonify(detail="Register Sec welcome"), 200
    else:
        return jsonify(detail="Email not found"), 404


@bp.route('/login', methods=(["POST"]))
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    check_user = User.query.filter(User.username == username).first()
    if check_user == None:
        return jsonify(detail="Error! User not found"), 404
    check_password = bc.check_password_hash(check_user.password, password)
    if check_user and check_password:
        return jsonify(detail="Welcome"), 200
    else:
        return jsonify(detail="Error! User not found"), 404
