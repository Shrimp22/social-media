from flask import Blueprint, jsonify, request, session
from db import db
from model import User

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




