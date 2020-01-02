from flask import jsonify, request, url_for, g, abort
from app import db
from app.models import WaterLog, WaterRequest
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request
import json

@bp.route('/water/<int:device_id>', methods=['GET'])
#@token_auth.login_required
def get_water(device_id):
    request = WaterRequest.query.filter_by(device_id=device_id, status=1).first_or_404()

    if request:
        request.status = False
        db.session.commit()

    return jsonify(request.duration),200

@bp.route('/water/log', methods=['POST'])
#@token_auth.login_required
def post_log():
    request_headers = request.headers.environ
    request_json = json.loads(request.data)
    try:
        log = WaterLog(duration=request_json['duration'],device_id=request_json['device_id'])
        db.session.add(log)
        db.session.commit()
    except:
        return 'Error',500
    
    return 'Created',201


@bp.route('/water/request', methods=['POST'])
#@token_auth.login_required
def post_request():
    request_headers = request.headers.environ
    request_json = json.loads(request.data)
    try:
        log = WaterRequest(duration=request_json['duration'],device_id=request_json['device_id'],status=True)
        db.session.add(log)
        db.session.commit()
    except:
        return 'Error',500
    
    return 'Created',201

