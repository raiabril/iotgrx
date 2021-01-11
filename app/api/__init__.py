from flask import Blueprint
from flask_restful import Api

bp = Blueprint('api', __name__)
bp_api = Api(bp)

from app.api import events, users, errors, tokens, water, sensors, devices