from flask import Flask
from flask_cors import CORS
from .controllers.shortUrlController import controller
from .repositories.shortUrlRepository import init_db
def create_app():
    app = Flask(__name__)
    init_db()
    app.register_blueprint(controller)
    CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:8000", "https://short-url-dp9s.onrender.com"]}})
    return app