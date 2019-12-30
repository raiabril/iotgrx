from flask import jsonify, request, url_for, g, abort
from flask import g
from flask_login import current_user
from app import db
from app.models import Event
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request

@bp.route('/events', methods=['GET'])
@token_auth.login_required
def get_events():
    data = [x.to_dict() for x in Event.query.all()]
    return jsonify(data)

@bp.route('/events', methods=['POST'])
#@token_auth.login_required
def post_events():
    print(request.get_json())
    data = request.get_json()["data"]

    for event in data:
        event_created = Event(
                            value=event['value'],
                            sensor_id = event['sensor_id'],
                            user_id = 1)
        db.session.add(event_created)
        db.session.commit()

    return 'OK',201