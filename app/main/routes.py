from flask import render_template, request, Blueprint, redirect, url_for, flash
from flask_login import current_user, login_required
from sqlalchemy import func
from app.models import Sensor, Event, Device, User
from app.main.utils import filter_values
from app.main.forms import RealValueForm
from app import db

main = Blueprint('main', __name__)

@main.route("/")
def home():
    if current_user.is_authenticated:
        devices = Device.query.filter_by(active=1).all()
        return render_template('index.html', 
                            title='iotGRX', 
                            devices=devices)
    else:
        return redirect(url_for('users.login'))


@main.route('/sensor/<int:sensor_id>', methods=['GET','POST'])
@login_required
def sensor(sensor_id):

    form = RealValueForm()

    if form.validate_on_submit():
        event = Event.query.get(form.id.data)
        event.real_value = form.real_value.data
        db.session.commit()
        flash('Real value updated and calibration regenerated!','success')
        return redirect(url_for('main.sensor', sensor_id = sensor_id))

    elif request.method == 'GET':
        devices = Device.query.filter_by(active=1).all()
        sensor = Sensor.query.get(sensor_id)
        device = Device.query.get(sensor.device_id)
        events = Event.query.filter_by(sensor_code=sensor.code)\
            .order_by(Event.date_created.desc())\
            .limit(2*24*7).all()

        form.id.data = events[0].id
        form.real_value.data = events[0].real_value
        form.calibrated.data = "{:.2f}".format(events[0].value*sensor.a1 + sensor.a0)

    greenFill = "rgba(151,220,150,0.3)"
    greenLine = "rgba(73,193,71,1)"
    yellowFill = "rgba(245,240,50,0.3)"
    yellowLine = "rgba(240,245,50,1)"
    #redFill = "rgba(234,121,106,0.3)"
    #redLine = "rgba(210,50,28,1)"
    #real_radius = 2

    labels=[]
    values=[]
    real_events = []

    # Events
    if events.__len__() > 1:
        for event in events:
            labels.append(event.date_created.strftime('%Y-%m-%d %H:%M:%S'))
            values.append(event.value)

            if event.real_value != None:
                real_events.append(event)
            
    # Filter values
    values = filter_values(values)

    # Apply calibration
    values = ["{:10.3f}".format(x*sensor.a1 + sensor.a0) for x in values]

    # Last event for display
    last_event = events[0]

    # Color for main graph
    if sensor.watering_trigger and sensor.watering_level < last_event.value:
        colorFill = yellowFill
        colorLine = yellowLine
    else:
        colorFill = greenFill
        colorLine = greenLine

    # Real events and fit
    real_values = [x.real_value for x in real_events]
    real_labels = [x.value for x in real_events]
    
    if len(real_values) <= 1:
        real_labels_fit = [-2000, 0, 2000]
        real_values_fit = [x*sensor.a1 + sensor.a0 for x in real_labels_fit]
    
    else:
        real_values_fit = [x.value*sensor.a1 + sensor.a0 for x in real_events]
        real_labels_fit = real_labels

    real_bubbles = list(zip(real_labels, real_values))
    real_fit = list(zip(real_labels_fit, real_values_fit))

    if sensor.watering_trigger:
        trigger_labels = [labels[0], labels[-1]]
        trigger_values = [sensor.watering_level*sensor.a1 + sensor.a0, sensor.watering_level*sensor.a1 + sensor.a0]
        water_trigger = list(zip(trigger_labels, trigger_values))
    else:
        water_trigger = []

    return render_template('chart.html', 
                            devices=devices,
                            sensor=sensor,
                            device=device,
                            labels=labels,
                            values=values,
                            real_bubbles=real_bubbles,
                            real_fit = real_fit,
                            water_trigger=water_trigger,
                            last_event=last_event,
                            colorFill=colorFill,
                            colorLine=colorLine,
                            title=device.name + " - " + sensor.name,
                            form=form)