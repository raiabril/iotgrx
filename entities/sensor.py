# coding=utf-8

from marshmallow import Schema, fields

from sqlalchemy import Column, String, Float, DateTime, Integer, ForeignKey

from .entity import Entity, Base
from .device import Device


class Sensor(Entity, Base):
    __tablename__ = 'sensors'

    pin = Column(Integer)
    name = Column(String)
    value_max = Column(Integer)
    value_min = Column(Integer)
    device_id = Column(Integer, ForeignKey(Device.id))

    def __init__(self, pin, name, device_id, value_max, value_min, created_by):
        Entity.__init__(self, created_by)
        self.pin = pin
        self.name = name
        self.device_id = device_id
        self.value_max = value_max
        self.value_min = value_min


class SensorSchema(Schema):
    id = fields.Integer()
    pin = fields.Integer()
    name = fields.Str()
    value_max = fields.Integer()
    value_min = fields.Integer()
    device_id = fields.Integer()

    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
