from flask import Flask
from backend.models.models import db
from backend.blueprints.auth_bp import bp as auth_bp, bcrypt, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    with app.app_context():
        db.create_all()

    bcrypt.init_app(app)
    jwt.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)

    # Register shipping blueprint
    from backend.blueprints.shipping_bp import bp as shipping_bp
    app.register_blueprint(shipping_bp)

    # Register auth blueprint
    app.register_blueprint(auth_bp)

    return app
