from flask import Blueprint

# Create blueprint
rentals = Blueprint('rentals', __name__)

from . import routes, models
