from flask import Blueprint

# Create blueprint
auth = Blueprint('auth', __name__)

from . import routes
