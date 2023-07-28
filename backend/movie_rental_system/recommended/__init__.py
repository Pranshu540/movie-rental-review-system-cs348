from flask import Blueprint

# Create blueprint
recommended = Blueprint('recommended', __name__)

from . import routes, models
