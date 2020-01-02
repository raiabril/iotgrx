from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import func
from app.models import WaterLog, WaterRequest
from app.water.forms import WaterForm

water = Blueprint('water', __name__)

@water.route("/check",methods=['GET','POST'])
def check():
    requests = WaterRequest.query.all()
    log = WaterLog.query.all()
    form = WaterForm()

    if form.validate_on_submit():
        return redirect(url_for('water.check'))

    return render_template('water.html', 
                            title='iotHome', 
                            requests=requests,
                            log=log)