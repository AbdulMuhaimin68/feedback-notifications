# main.py

from flask import Flask
from app.extensions.extensions import db, ma, mail, migrate
from config import Config
from flask_jwt_extended import JWTManager

jwt = JWTManager()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    

    # Register Blueprints
    from app.Blueprint.User_blueprint import bp as user_bp
    from app.Blueprint.login_blueprint import bp as user_login_bp
    from app.Blueprint.Feedback_blueprint import bp as feedback_bp
    app.register_blueprint(user_bp)
    app.register_blueprint(user_login_bp)
    app.register_blueprint(feedback_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
