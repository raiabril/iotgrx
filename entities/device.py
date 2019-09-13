# coding=utf-8

from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer
from .entity import Entity, Base


class Device(Entity, Base):
    __tablename__ = 'devices'

    title = Column(String)
    host = Column(String)
    port = Column(Integer)

    def __init__(self, title, host, port, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.host = host
        self.port = port


class DeviceSchema(Schema):
    id = fields.Integer()
    title = fields.Str()
    host = fields.Str()
    port = fields.Integer()

    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()

