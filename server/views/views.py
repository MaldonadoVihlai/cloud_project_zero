from flask import request
from ..models import *
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, \
                               unset_jwt_cookies, jwt_required, JWTManager
                               
user_schema = UserSchema()
event_schema = EventSchema()

class ViewSignIn(Resource):
    
    def post(self):
        new_user = UserModel(email=request.json["email"], password=generate_password_hash(request.json["password"], method='sha256'))
        db.session.add(new_user)
        try:
            db.session.commit()
            access_token = create_access_token(identity=new_user.id)
            response = {"access_token":access_token, "msg": 200}
            return response
        except IntegrityError:
            db.session.rollback()
            return 'El email ya existe ',409


    def put(self, id_user):
        user = UserModel.query.get_or_404(id_user)
        user.password = request.json.get("password",user.password)
        db.session.commit()
        return user_schema.dump(user)

    def delete(self, id_user):
        user = UserModel.query.get_or_404(id_user)
        db.session.delete(user)
        db.session.commit()
        return '',204

class ViewLogIn(Resource):
    
    def post(self):
        user = UserModel.query.filter_by(email = request.json["email"]).first()
        if not user or not check_password_hash(user.password, request.json["password"]):
            return "Unauthorized", 401
        access_token = create_access_token(identity=user.id)
        response = {"access_token":access_token, "msg": 200, "id": user.id}
        return response
	    



class ViewEvent(Resource):
    @jwt_required() 
    def get(self, id_event):
        return event_schema.dump(EventModel.query.get_or_404(id_event))
    
    @jwt_required() 
    def put(self, id_event):
        event = EventModel.query.get_or_404(id_event)
        event.name = request.json.get("name",event.name)
        event.category = request.json.get("category", event.category)
        event.place = request.json.get("place", event.place)
        event.address = request.json.get("address", event.address)
        event.start_date = request.json.get("start_date", event.start_date)
        event.end_date = request.json.get("end_date", event.end_date)
        event.virtual = request.json.get("virtual", event.virtual)
        db.session.commit()
        return event_schema.dump(event)

    def delete(self, id_event):
        event = EventModel.query.get_or_404(id_event)
        db.session.delete(event)
        db.session.commit()
        return '',204

def str_to_bool(s):
    if s == 'True':
         return True
    elif s == 'False':
         return False
    else:
         raise ValueError
class ViewAEventsUser(Resource):
    @jwt_required()
    def post(self, id_user):
        new_event = EventModel(name=request.json["name"], category=request.json["category"], place=request.json["place"], 
                                address=request.json["address"], start_date=request.json["start_date"], end_date=request.json["end_date"], 
                                virtual=request.json["virtual"])
        user = UserModel.query.get_or_404(id_user)
        user.events.append(new_event)

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return 'El usuario ya tiene un evento con dicho nombre',409

        return event_schema.dump(new_event)
    @jwt_required()
    def get(self, id_user):
        user = UserModel.query.get_or_404(id_user)
        return [event_schema.dump(ev) for ev in user.events]
