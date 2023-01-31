from flask import Flask
from datetime import timedelta

def create_app(config_name):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Project 0"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_RUN_PORT'] = 5001
    app.config['JWT_ACCESS_TOKEN_EXPIRES']=timedelta(minutes=20)
    app.config['JWT_REFRESH_TOKEN_EXPIRES']=timedelta(minutes=20)
    app.config['JWT_SECRET_KEY']='f4fa6e8c8cae260aa655f92e'
    return app
