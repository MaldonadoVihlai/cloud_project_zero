from marshmallow import Schema, fields


class User_Schema(Schema):
    class Meta:
        fields = ("id", "email", "password", "events")


class Event_Schema(Schema):
    class Meta:
        fields = ("id", "name", "category", "place", "address",
                  "start_date", "end_date", "virtual")
