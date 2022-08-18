from flask import Flask
from flask_cors import CORS

from src.views import api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    CORS(app)

    return app
