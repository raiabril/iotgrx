# coding=utf-8

from marshmallow import Schema, fields

from sqlalchemy import Column, ForeignKey, Integer

from .entity import Entity, Base
from .sensor import Sensor


class Event(Entity, Base):
    __tablename__ = 'events'

    sensor_id = Column(Integer, ForeignKey(Sensor.id))
    value = Column(Integer)

    def __init__(self, sensor_id, value, created_by):
        Entity.__init__(self, created_by)
        self.sensor_id = sensor_id
        self.value = value


class EventSchema(Schema):
    id = fields.Integer()
    sensor_id = fields.Integer()
    value = fields.Integer()

    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
