from flask import Blueprint, jsonify, request
from db import db
from model import User

bp = Blueprint('user_menagament',__name__, url_prefix="/admin")

@bp.route('/list-users', methods=[("GET")])
def list_users():
    
