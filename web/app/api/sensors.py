from flask import jsonify, request, url_for, g, abort
from flask import g
from flask_login import current_user
from app import db
from app.models import Sensor
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request

@bp.route('/sensors', methods=['GET'])
@token_auth.login_required
def get_sensors():
    data = [x.to_dict() for x in Sensor.query.all()]
    return jsonify(data)


@bp.route('/sensors/<int:sensor_id>', methods=['GET'])
@token_auth.login_required
def get_sensor_id(sensor_id):
    return jsonify(Sensor.query.filter_by(id=sensor_id).first_or_404().to_dict())