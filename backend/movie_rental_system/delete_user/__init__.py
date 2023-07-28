from flask import Blueprint

# Create blueprint
delete_user = Blueprint('delete_user', __name__)

from . import routes, models
