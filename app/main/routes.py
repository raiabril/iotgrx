from flask import render_template, request, Blueprint
from flask_login import current_user, login_required
from sqlalchemy import func
from app.models import Sensor, Event, Device

main = Blueprint('main', __name__)

@main.route("/")
def home():
    sensors = Sensor.query.all()
    return render_template('index.html', title='iotHome', sensors=sensors)


@main.route('/sensor/<int:sensor_id>')
def sensor(sensor_id):
    sensors = Sensor.query.all()
    sensor = Sensor.query.filter_by(id=sensor_id).first_or_404()
    events = Event.query.filter_by(sensor_id=sensor_id).all()

    labels=[]
    values=[]
    for event in events:
        labels.append(event.date_created.strftime('%Y-%m-%d %H:%M:%S'))
        values.append(event.value)
    
    updated_time = labels[-1]
    updated_value = values[-1]

    return render_template('chart.html', 
                            sensors=sensors,
                            title=sensor.name,
                            labels=labels,
                            values=values,
                            updated_time=updated_time,
                            updated_value=updated_value)