# coding: utf8
from marshmallow import (Schema, fields)


class LocationSchema(Schema):
    id = fields.String()
    name = fields.String()
    latitude = fields.Decimal()
    longitude = fields.Decimal()


class StationSchema(Schema):
    id = fields.String()
    location = fields.Nested(LocationSchema)
    order = fields.Integer()
    is_active = fields.Boolean()


class LineSchema(Schema):
    id = fields.String()
    name = fields.String()
    color = fields.String()


class RouteSchema(Schema):
    id = fields.String()
    line = fields.Nested(LineSchema)
    stations = fields.Nested(StationSchema)
    direction = fields.Boolean()
    is_active = fields.Boolean()
