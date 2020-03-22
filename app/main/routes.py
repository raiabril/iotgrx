from flask import render_template, request, Blueprint, redirect, url_for
from flask_login import current_user, login_required
from sqlalchemy import func
from app.models import Sensor, Event, Device, User
from app.main.utils import filter_values

main = Blueprint('main', __name__)

@main.route("/")
def home():
    if current_user.is_authenticated:
        devices = Device.query.filter_by(active=1).all()
        return render_template('index.html', 
                            title='iotHome', 
                            devices=devices)
    else:
        return redirect(url_for('users.login'))


@main.route('/sensor/<int:sensor_id>')
@login_required
def sensor(sensor_id):

    greenFill = "rgba(151,220,150,0.3)"
    greenLine = "rgba(73,193,71,1)"
    yellowFill = "rgba(245,240,50,0.3)"
    yellowLine = "rgba(240,245,50,1)"
    redFill = "rgba(234,121,106,0.3)"
    redLine = "rgba(210,50,28,1)"

    devices = Device.query.filter_by(active=1).all()
    sensor = Sensor.query.filter_by(id=sensor_id).first_or_404()
    events = Event.query.filter_by(sensor_code=sensor.code)\
            .order_by(Event.date_created.desc())\
            .limit(2*24*7).all()

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

        for event in events:
            labels.append(event.date_created.strftime('%Y-%m-%d %H:%M:%S'))
            values.append(event.value)
            
        # Filter values
        values = filter_values(values)
        updated_time = labels[0]
        updated_value = values[0]

        if updated_value < 2800:
            colorFill=greenFill
            colorLine=greenLine
        elif updated_value < 3500:
            colorFill=yellowFill
            colorLine=yellowLine
        else:
            colorFill=redFill
            colorLine=redLine

    return render_template('chart.html', 
                            devices=devices,
                            title=sensor.name,
                            labels=labels,
                            values=values,
                            updated_time=updated_time,
                            updated_value=updated_value,
                            colorFill=colorFill,
                            colorLine=colorLine)