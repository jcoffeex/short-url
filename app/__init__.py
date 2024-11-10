from flask import Flask
from flask_cors import CORS
from .views import views
from .models import init_db
def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5000"]}})
    init_db()
    app.register_blueprint(views)
    
    return app