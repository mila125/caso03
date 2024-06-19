from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    db.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()

    from .views import views_bp
    app.register_blueprint(views_bp)

    return app
