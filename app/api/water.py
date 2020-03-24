from flask import jsonify, request, url_for, g, abort
from app import db
from app.models import WaterLog, WaterRequest
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request
import json

@bp.route('/water/<string:device_code>', methods=['GET'])
#@token_auth.login_required
def get_water_request(device_code):
    request = WaterRequest.query.filter_by(device_code=device_code, pending=1).first_or_404()

    if request:
        request.pending = False
        db.session.commit()

    return jsonify(request.duration),200


@bp.route('/water/log/<string:device_code>', methods=['GET'])
@token_auth.login_required
def get_water_log(device_code):
    request = [x.to_dict() for x in WaterLog.query.filter_by(device_code=device_code).order_by(WaterLog.date_created.desc()).limit(10)]
    return jsonify(request),200


@bp.route('/water/log', methods=['POST'])
#@token_auth.login_required
def post_log():
    request_headers = request.headers.environ
    request_json = json.loads(request.data)

    try:
        log = WaterLog(duration=request_json['duration'],device_code=request_json['device_code'])
        db.session.add(log)
        db.session.commit()
    except:
        return 'Error',500
    
    return 'Created',201


@bp.route('/water/request', methods=['POST'])
@token_auth.login_required
def post_request():
    request_headers = request.headers.environ
    request_json = json.loads(request.data)
    try:
        log = WaterRequest(duration=request_json['duration'],
                            device_code=request_json['device_code'],
                            pending=True, 
                            creator = 'API')
        db.session.add(log)
        db.session.commit()
    except:
        return 'Error',500
    
    return 'Created',201

