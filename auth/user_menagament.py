from flask import Blueprint, jsonify, request, session
from db import db
from model import User
#from flask_bcrypt import Bcrypt
from .auth import bc
#bc = Bcrypt()
bp = Blueprint('user_menagament',__name__, url_prefix="/admin")
# Helper function to check user status is admin or not (boolean type)
def is_admin(user):
    get_user = User.query.filter(User.username == user).first()
    is_admin = get_user.is_admin
    if is_admin:
        return True
    else:
        return False


@bp.route('/list-users', methods=[("GET")])
def list_users():
    username = session.get('username')
    if is_admin(username):
        get_users = User.query.all()
        users_list = []
        for user in get_users:
            if user.username != username:
                users_list.append(user.username)
        return jsonify(users=users_list), 200
    else:
        return jsonify(detail="User is not admin"), 400



@bp.route('/delete', methods=[("POST")])
def delete_user():
    username = session.get('username')
    username_delete = request.json.get('username')
    if is_admin(username):
        delete_query = User.query.filter(User.username == username_delete).first()
        db.session.delete(delete_query)
        db.session.commit()
        return jsonify(detail="User was deleted"), 200
    else:
        return jsonify(detail="Error! You are not admin"), 409



@bp.route('/update-password', methods=[("POST")])
def update_passowrd():
    username = session.get('username')
    user_for_change = request.json.get('username_for_change')
    new_password = request.json.get('new_pw')
    get_username = User.query.filter(User.username == user_for_change).first()
    if is_admin(username):
        hash_pw = bc.generate_password_hash(new_password)
        get_username.password = hash_pw
        db.session.commit()
        return jsonify(detail="Password was changed"), 200
    else:
        return jsonify(detail="Error! You are not admin"), 409

@bp.route('/update-username', methods=[("POST")])
def update_username():
    username = session.get('username')
    username_for_change = request.json.get('username_for_change')
    new_username = request.json.get('new_username')
    if is_admin(username):
        get_username = User.query.filter(User.username == username_for_change).first()
        get_username.username = new_username
        db.session.commit()
        return jsonify(detail = "Username was changed"), 200

    else:
        return jsonify(detail = "You are not admin"), 409

