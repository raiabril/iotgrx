from flask import jsonify, request, url_for, g, abort
from app import db
from app.models import Event
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request

@bp.route('/water', methods=['GET'])
@token_auth.login_required
def get_water():
    return 'OK',200