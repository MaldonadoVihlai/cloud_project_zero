from ..db import db
import enum
from sqlalchemy import Enum
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Category(enum.Enum):
    Conferencia = 1
    Seminario = 2
    Congreso = 3
    Curso = 4


class EventModel(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    category = db.Column(Enum(Category), unique=False, nullable=True)
    place = db.Column(db.String(64), unique=False, nullable=True)
    address = db.Column(db.String(256), unique=False, nullable=True)
    start_date = db.Column(db.String(64), unique=False, nullable=True)
    end_date = db.Column(db.String(64), unique=False, nullable=True)
    virtual = db.Column(db.Boolean, unique=False, nullable=True)

    user = db.Column(db.Integer, db.ForeignKey("users.id"))

class EnumToDict(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return value.name

class EventSchema(SQLAlchemyAutoSchema):
    category = EnumToDict(attribute=("category"))
    class Meta:
         model = EventModel
         include_relationships = True
         load_instance = True