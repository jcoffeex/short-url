from flask import Flask
from flask_cors import CORS
from .views import views
from .models import init_db
def create_app():
    app = Flask(__name__)
    init_db()
    app.register_blueprint(views)
    CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:8000", "https://short-url-dp9s.onrender.com"]}})
    return app