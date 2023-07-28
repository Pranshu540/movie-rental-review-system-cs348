from flask import Blueprint

# Create blueprint
reviews = Blueprint('reviews', __name__)

from . import routes, models
