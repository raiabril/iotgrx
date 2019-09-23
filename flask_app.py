# A very simple Flask Hello World app for you to get started with...

# coding=utf-8
import datetime
import logging
import time
import requests
import socket
from logging.handlers import RotatingFileHandler
import json
from flask import Flask, jsonify, request, render_template

from aux import format_date, get_color, filter_values
from credentials import local_url, device_host, device_port
from entities.device import Device, DeviceSchema
from entities.entity import Session, engine, Base
from entities.event import Event, EventSchema
from entities.sensor import Sensor, SensorSchema
from query import get_sensors_query, get_events_query, get_devices_query, get_sensor_query

app = Flask(__name__, static_url_path='/static')

# if needed, generate database schema
Base.metadata.create_all(engine)

# Activating logs
handler = RotatingFileHandler('iotBackend.log', maxBytes=10000, backupCount=1)
app.logger.addHandler(handler)

log = logging.getLogger('werkzeug')
log.addHandler(handler)


# ------------------- WEBSITE -------------------

@app.route('/')
@app.route('/index')
def index():
    sensor_list = get_sensors_query()
    return render_template('index.html', sensors=sensor_list, title="iotHome")


@app.route('/sensor/<int:sensor_id>')
def sensor(sensor_id):
    event_list = get_events_query(sensor_id, '2019-01-01', '2020-01-01', 288)
    sensor_list = get_sensors_query()
    sensor_object = next((item for item in sensor_list if item['id'] == sensor_id), None)
    labels = [event['created_at'] for event in event_list]
    values = [event['value'] for event in event_list]
    values = filter_values(values)
    colorFill, colorLine = get_color(int(values[::-1][-1]))

    return render_template('chart2.html',
                           values=values[::-1],
                           labels=labels[::-1],
                           max=4096,
                           sensors=sensor_list,
                           title=' AIO' +
                                 str(sensor_object['pin']) + " - " +
                                 sensor_object['name'],
                           colorFill=colorFill,
                           colorLine=colorLine)


@app.route('/device/<int:device_id>/tasks')
def water(device_id):
    sensor_list, errors = get_sensors_query()
    time.sleep(10)
    # DeviceController(local_url, device_host, device_port).start_water()
    # DeviceController(local_url, device_host, device_port).stop_water()
    return render_template("json.html",
                           title="Result",
                           code='Done!',
                           sensors=sensor_list)


# ------------------- SERVICES -------------------

@app.route('/api/v1.0/devices')
def get_devices():
    # fetching from the database
    result = get_devices_query()
    return jsonify(result), 200


@app.route('/api/v1.0/devices', methods=['POST'])
def add_device():
    posted_object = DeviceSchema(only=('title', 'host', 'port')).load(request.get_json())
    json_object = Device(**posted_object, created_by="HTTP post request")

    # persist exam
    session = Session()
    session.add(json_object)
    session.commit()

    # return created exam
    new_object = DeviceSchema().dump(json_object)
    session.close()
    return jsonify(new_object), 201


@app.route('/api/v1.0/sensors')
def get_sensors():
    result = get_sensors_query()
    return jsonify(result), 200


@app.route('/api/v1.0/sensors/<int:sensor_id>')
def get_sensor(sensor_id):
    result = get_sensor_query(sensor_id)
    return jsonify(result), 200


@app.route('/api/v1.0/sensors', methods=['POST'])
def add_sensor():
    data = request.get_json()["sensor"]
    new_object_list = []

    for dat in data:
        posted_object = SensorSchema(only=('pin', 'name', 'device_id', 'value_max', 'value_min')) \
            .load(dat)

        json_object = Sensor(**posted_object, created_by="HTTP post request")
        session = Session()
        session.add(json_object)
        session.commit()
        new_object_list.append(SensorSchema().dump(json_object))
        session.close()

    return jsonify(new_object_list), 201


@app.route('/api/v1.0/events')
def get_events():
    # Get sensor_id
    sensor_id = request.args.get('sensor_id', default='*')
    from_date = request.args.get('from', default='2019-01-01')
    to_date = request.args.get('to', default=datetime.datetime.now().isoformat())
    req_limit = request.args.get('limit', default=100)

    result = get_events_query(sensor_id, from_date, to_date, req_limit)

    return jsonify(result), 200


@app.route('/api/v1.0/events', methods=['POST'])
@app.route('/events', methods=['POST'])
def add_events():
    data = request.get_json()["data"]
    new_object_list = []

    for dat in data:
        posted_object = EventSchema(only=("sensor_id", 'value')).load(dat)
        json_object = Event(**posted_object, created_by="HTTP post request")
        session = Session()
        session.add(json_object)
        session.commit()
        new_object_list.append(EventSchema().dump(json_object))
        session.close()

    return jsonify(new_object_list), 201
