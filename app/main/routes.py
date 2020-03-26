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

    greenFill = "rgba(151,220,150,0.3)"
    greenLine = "rgba(73,193,71,1)"
    yellowFill = "rgba(245,240,50,0.3)"
    yellowLine = "rgba(240,245,50,1)"
    redFill = "rgba(234,121,106,0.3)"
    redLine = "rgba(210,50,28,1)"

    if events.__len__() <= 1:
        labels=[]
        values=[]
        updated_time="";
        updated_value="";
        colorFill="";
        colorLine="";

    else:
        labels=[]
        values=[]
        real_value = []

        for event in events:
            labels.append(event.date_created.strftime('%Y-%m-%d %H:%M:%S'))
            values.append(event.value)
            real_value.append(event.real_value)
            
        # Filter values
        values = filter_values(values)
        updated_time = labels[0]
        updated_value = values[0]
        updated_value_raw = values[0]
        updated_real_value = real_value[0]

        if updated_value < 2800:
            colorFill=greenFill
            colorLine=greenLine
        elif updated_value < 3500:
            colorFill=yellowFill
            colorLine=yellowLine
        else:
            colorFill=redFill
            colorLine=redLine

        updated_value = "{:10.2f}".format(updated_value*sensor.a1 + sensor.a0)
        values = [x*sensor.a1 + sensor.a0 for x in values]
        values = ["{:10.3f}".format(x) for x in values]

    return render_template('chart.html', 
                            devices=devices,
                            sensor=sensor,
                            device=device,
                            labels=labels,
                            values=values,
                            updated_time=updated_time,
                            updated_value=updated_value,
                            updated_real_value=updated_real_value,
                            updated_value_raw=updated_value_raw,
                            colorFill=colorFill,
                            colorLine=colorLine,
                            title=device.name + " - " + sensor.name,
                            form=form)