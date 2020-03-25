from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import func
from app.models import WaterLog, WaterRequest, Device, Sensor, Event
from app.water.forms import WaterForm
from app import db

water = Blueprint('water', __name__)

@water.route("/check/<string:device_code>", methods=['GET','POST'])
@login_required
def check(device_code):
    device = Device.query.filter_by(code=device_code).first()
    devices = Device.query.filter_by(active=1).all()
    requests = WaterRequest.query.filter_by(pending=True).order_by(WaterRequest.date_created.asc()).all()
    logs = WaterLog.query.filter_by(device_code=device.code).order_by(WaterLog.date_created.desc()).limit(10).all()
    form = WaterForm()
    event = Event.query.filter_by(device_code=device.code).order_by(Event.date_created.desc()).first()

    if form.validate_on_submit():
        duration = form.duration.data
        request = WaterRequest(device_code=device.code, pending=True, duration=duration, creator='Web')
        db.session.add(request)
        db.session.commit()
        flash('Watering requested!','success')
        return redirect(url_for('water.check', device_code=device.code))

    return render_template('water.html', 
                            title=device.name + " - water system", 
                            requests=requests,
                            logs=logs,
                            form=form,
                            device=device,
                            devices=devices,
                            event=event)