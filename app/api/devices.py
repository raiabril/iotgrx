from flask import jsonify, request, url_for, g, abort
from flask import g
from flask_login import current_user
from app import db
from app.models import Device
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request

@bp.route('/devices', methods=['GET'])
@token_auth.login_required
def get_devices():
    data = [x.to_dict() for x in Device.query.filter_by(user_id=g.current_user.id).all()]
    return jsonify(data)