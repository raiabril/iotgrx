from entities.entity import Session, engine, Base
from entities.event import Event, EventSchema
from entities.sensor import Sensor, SensorSchema
from entities.device import Device, DeviceSchema
from credentials import local_url, device_host, device_port


def get_devices_query():
    # fetching from the database
    session = Session()
    device_objects = session.query(Device).all()

    # transforming into JSON-serializable objects
    schema = DeviceSchema(many=True)
    result = schema.dump(device_objects)

    # serializing as JSON
    session.close()
    return result


def get_events_query(sensor_id, from_date, to_date, req_limit):
    session = Session()
    result_objects = session.query(Event).filter(Event.sensor_id == sensor_id) \
        .order_by(Event.created_at.desc()) \
        .filter(Event.created_at > from_date, Event.created_at <= to_date) \
        .with_entities(Event.created_at, Event.value) \
        .limit(req_limit)

    # transforming into JSON-serializable objects
    schema = EventSchema(many=True)
    result = schema.dump(result_objects)

    session.close()
    return result


def get_sensors_query():
    session = Session()
    result_objects = session.query(Sensor).all()

    # transforming into JSON-serializable objects
    schema = SensorSchema(many=True)
    result = schema.dump(result_objects)

    session.close()
    return result
