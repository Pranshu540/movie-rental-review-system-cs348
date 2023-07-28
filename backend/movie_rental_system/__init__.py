from flask import Flask
from .settings import Config
from flask_mysqldb import MySQL


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # Initialize MySQL
    mysql = MySQL(app)

    # Add MySQL object to app's configuration
    app.config['mysql'] = mysql

    # Now init app
    # mysql.init_app(app)

    # import and register blueprints
    from .auth import auth as auth_blueprint
    from .filter_movie import filter_movie as filter_movie_blueprint
    from .reviews import reviews as reviews_blueprint
    from .rentals import rentals as rentals_blueprint
    from .delete_user import delete_user as delete_user_blueprint
    from .recommended import recommended as recommended_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(filter_movie_blueprint, url_prefix='/filter_movie')
    app.register_blueprint(reviews_blueprint, url_prefix='/reviews')
    app.register_blueprint(rentals_blueprint, url_prefix='/rentals')
    app.register_blueprint(delete_user_blueprint, url_prefix='/delete_user')
    app.register_blueprint(recommended_blueprint, url_prefix='/recommended')

    return app
