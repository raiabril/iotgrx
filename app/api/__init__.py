from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import events, users, errors, tokens, water