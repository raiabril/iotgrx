from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import func
from app.models import WaterLog, WaterRequest, Device
from app.water.forms import WaterForm
from app import db

water = Blueprint('water', __name__)

@water.route("/check",methods=['GET','POST'])
def check():
    requests = WaterRequest.query.filter_by(status=True).order_by(WaterRequest.date_created.desc()).all()
    devices = Device.query.all()
    logs = WaterLog.query.order_by(WaterLog.date_created.desc()).all()
    form = WaterForm()

    if form.validate_on_submit():
        request = WaterRequest(duration=1000,device_id=1,status=True)
        db.session.add(request)
        db.session.commit()
        return redirect(url_for('water.check'))

    return render_template('water.html', 
                            title='iotHome', 
                            requests=requests,
                            logs=logs,
                            form=form,
                            devices=devices)