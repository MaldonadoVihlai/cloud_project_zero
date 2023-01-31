from server import create_app
from flask_restful import Api
from .db import db
from . import models
from . import views
from datetime import datetime 
from flask_cors import CORS
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, \
                               unset_jwt_cookies, jwt_required, JWTManager

app = create_app('default')
CORS(app)
jwt = JWTManager(app)

app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(views.ViewSignIn, '/signup')
api.add_resource(views.ViewLogIn, '/login')
api.add_resource(views.ViewAEventsUser, '/user/<int:id_user>/events')
api.add_resource(views.ViewEvent, '/event/<int:id_event>')
# with app.app_context():
#     pass
#     u = models.UserModel(email='vihlai@hotmail.com', password='12345')
#     e = models.EventModel(name='Prueba', category=models.Category.Conferencia,place='Bogota', address='Calle 1',start_date=datetime.now(), end_date=datetime.now(), virtual=True)
#     u.events.append(e)
#     db.session.add(u)
#     db.session.commit()
#     print(models.UserModel.query.all())
#     print(models.EventModel.query.all())
