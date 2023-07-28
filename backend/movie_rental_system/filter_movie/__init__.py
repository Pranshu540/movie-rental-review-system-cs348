from flask import Blueprint

# Create blueprint
filter_movie = Blueprint('filter_movie', __name__)

from . import routes
