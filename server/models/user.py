from ..db import db
from uuid import uuid4
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True, unique = True)
    email = db.Column(db.String(345), unique=True, nullable=False)
    password = db.Column(db.Text, unique=False, nullable=False)
    events = db.relationship("EventModel", cascade='all, delete, delete-orphan')

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = UserModel
         include_relationships = True
         load_instance = True