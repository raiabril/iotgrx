from flask_restful import Resource
from flask import request
from app import db
from . import bp_api

from app.api.schemas.device import DeviceSchema
from app.models import Device

device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)

class DeviceResourceList(Resource):
    def get(self):
        devices = Device.query.all()
        return devices_schema.dump(devices)

    def post(self):
            new_device = Device(
                name=request.json['name'],
                code=request.json['code'],
                user_id=request.json['user_id']
            )
            db.session.add(new_device)
            db.session.commit()
            return device_schema.dump(new_device)


class DeviceResource(Resource):
    def get(self, device_id):
        device = Device.query.get_or_404(device_id)
        return device_schema.dump(device)

    def patch(self, device_id):
        device = Device.query.get_or_404(device_id)

        if 'default_watering' in request.json:
            device.default_watering = request.json['default_watering']
        if 'default_sleep' in request.json:
            device.default_sleep = request.json['default_sleep']

        db.session.commit()
        return device_schema.dump(device)

    def delete(self, device_id):
        device = Device.query.get_or_404(device_id)
        db.session.delete(device)
        db.session.commit()
        return '', 204

bp_api.add_resource(DeviceResourceList, '/devices')
bp_api.add_resource(DeviceResource, '/devices/<int:device_id>')