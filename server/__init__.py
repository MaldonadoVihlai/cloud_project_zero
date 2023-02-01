from flask import Flask
from .config import ApplicationConfig

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(ApplicationConfig)
    return app
