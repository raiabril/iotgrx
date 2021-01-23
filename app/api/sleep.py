from flask import jsonify, request, url_for, g, abort
from app import db
from app.models import Device
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request
import json

@bp.route('/sleep/<string:code>', methods=['GET'])
def get_sleep_request(code):
    sleep_time = Device.query.filter_by(code=code).first_or_404().default_sleep

    return jsonify(sleep_time),200