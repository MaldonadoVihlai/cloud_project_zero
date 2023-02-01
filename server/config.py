from dotenv import load_dotenv
import os
load_dotenv()
from datetime import timedelta

class ApplicationConfig:
    SECRET_KEY = os.environ["SECRET_KEY"]
    API_TITLE = "Project 0"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_RUN_PORT = 5001
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=20)
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(minutes=20)
    JWT_SECRET_KEY='f4fa6e8c8cae260aa655f92e'

