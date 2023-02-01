from server import create_app
from flask_restful import Api
from .db import db
from . import views
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = create_app('default')
CORS(app)
jwt = JWTManager(app)

app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(views.ViewSignUp, '/signup')
api.add_resource(views.ViewLogIn, '/login')
api.add_resource(views.ViewAEventsUser, '/user/<int:id_user>/events')
api.add_resource(views.ViewEvent, '/event/<int:id_event>')
