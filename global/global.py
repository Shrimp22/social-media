from flask import Blueprint, jsonify

bp = Blueprint('global', url_prefix='/global')

@bp.route('/not-found', methods=[("GET")])
def get_not_found():
    return jsonify(detail = "Not found"), 404
