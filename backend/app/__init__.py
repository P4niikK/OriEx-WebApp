from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from . import routes
    app.register_blueprint(routes.bp)

    # Register shipping blueprint
    from backend.blueprints.shipping_bp import bp as shipping_bp
    app.register_blueprint(shipping_bp)

    return app
