from flask import Blueprint, jsonify, request, session
from db import db
from model import User, Posts 
bp = Blueprint('post', url_prefix='/post')

@bp.route('/create-post', methods=[("POST")])
def create_post():
    
