from flask import render_template, request, Blueprint, redirect, url_for, flash
from flask_login import current_user, login_required
from sqlalchemy import func
from app.models import Sensor, Event, Device, User
from app.main.utils import filter_values, calibrate_raw, fit_curve
from app.main.forms import RealValueForm, WateringForm
from app import db
import numpy as np
import pandas as pd
import datetime

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
    sensor_form = WateringForm()

    if sensor_form.is_submitted() and sensor_form.submit2.data:

        sensor = Sensor.query.get(sensor_form.id.data)
        sensor.watering_trigger = sensor_form.trigger.data

        if sensor_form.level.data:
            sensor.watering_level = (sensor_form.level.data - sensor.a0)/sensor.a1

        else:
            sensor.watering_level = None

        sensor.name = sensor_form.name.data
        sensor.a0 = sensor_form.a0.data
        sensor.a1 = sensor_form.a1.data
        sensor.units = sensor_form.units.data
        sensor.sensor_type = sensor_form.sensor_type.data
        sensor.fit_type = sensor_form.fit_type.data
        
        db.session.commit()
        
        flash('Updated sensor configuration','success')
        return redirect(url_for('main.sensor', sensor_id = sensor_id))

    if form.is_submitted() and form.submit1.data:
        event = Event.query.get(form.id.data)
        sensor = Sensor.query.get(sensor_id)
        event.real_value = form.real_value.data
        real_events = Event.query.filter(Event.sensor_code==sensor.code).filter(Event.real_value!=None).all()

        if len(real_events) > 5:

            y = [event.real_value for event in real_events]
            x = [event.value for event in real_events]
            sensor.a0, sensor.a1 = fit_curve(x, y, sensor.fit_type)

        db.session.commit()

        flash('Real value updated and calibration regenerated!','success')
        return redirect(url_for('main.sensor', sensor_id = sensor_id))

    elif request.method == 'GET':
        time_frame = request.args.get('time', type=str)
        devices = Device.query.filter_by(active=1).all()
        sensor = Sensor.query.get(sensor_id)
        device = Device.query.get(sensor.device_id)
        real_events = Event.query.filter(Event.sensor_code==sensor.code).filter(Event.real_value!=None).all()

        if time_frame == '1d':
            events = Event.query.filter_by(sensor_code=sensor.code)\
                .filter(Event.date_created>datetime.datetime.now()-datetime.timedelta(days=1, hours=1))\
                .order_by(Event.date_created.desc()).all()


        elif time_frame == '1w':
            events = Event.query.filter_by(sensor_code=sensor.code)\
                .filter(Event.date_created>datetime.datetime.now()-datetime.timedelta(days=7))\
                .order_by(Event.date_created.desc()).all()


        elif time_frame == '1m':
            events = Event.query.filter_by(sensor_code=sensor.code)\
                    .filter(Event.date_created>datetime.datetime.now()-datetime.timedelta(weeks=4))\
                    .order_by(Event.date_created.desc()).all()


        elif time_frame == '1y':
            events = Event.query.filter_by(sensor_code=sensor.code)\
                .filter(Event.date_created>datetime.datetime.now()-datetime.timedelta(weeks=52))\
                .order_by(Event.date_created.desc()).all()


        else:
            events = Event.query.filter_by(sensor_code=sensor.code)\
            .order_by(Event.date_created.desc())\
            .limit(4*24*2).all()


        if len(events):
            form.id.data = events[0].id
            form.real_value.data = events[0].real_value
            form.value.data = events[0].value
            form.calibrated.data = "{:.2f}".format(calibrate_raw(events[0].value, sensor.a0, sensor.a1, sensor.fit_type))
        
        sensor_form.name.data = sensor.name
        sensor_form.a0.data = sensor.a0
        sensor_form.a1.data = sensor.a1
        sensor_form.id.data = sensor.id
        sensor_form.fit_type.data = sensor.fit_type
        sensor_form.sensor_type.data = sensor.sensor_type
        sensor_form.units.data = sensor.units

        if sensor.watering_level:
            sensor_form.level.data = sensor.watering_level*sensor.a1 + sensor.a0
        else:
            sensor_form.level.data = ""

        sensor_form.trigger.data = sensor.watering_trigger

        greenFill = "rgba(151,220,150,0.3)"
        greenLine = "rgba(73,193,71,1)"
        yellowFill = "rgba(245,240,50,0.3)"
        yellowLine = "rgba(240,245,50,1)"
        #redFill = "rgba(234,121,106,0.3)"
        #redLine = "rgba(210,50,28,1)"
        #real_radius = 2

        labels=[]
        values=[]
        values_avg = []
        values_max = []
        values_min = []
        values_rolling = []
        last_event = []
        real_bubbles = []
        real_fit = []
        water_trigger = []

        colorFill = yellowFill
        colorLine = yellowLine

        # Events
        if events.__len__() > 1:
            for event in events:
                labels.append(event.date_created.strftime('%Y-%m-%d %H:%M:%S'))
                values.append(event.value)
                
            # Pivot values
            dataframe = []

            # Apply calibration
            values = calibrate_raw(values, sensor.a0, sensor.a1, sensor.fit_type)

            for i in range(len(values)):
                dataframe.append([labels[i],values[i]])

            df = pd.DataFrame(dataframe)
            df.columns = ['date','value']
            df.date = pd.to_datetime(df.date)
            df.set_index('date', inplace=True)
            df.sort_index(inplace=True)            


            if time_frame == '1y':
                df_mean = df.groupby(pd.Grouper(freq='4D')).mean()
                df_max = df.groupby(pd.Grouper(freq='4D')).max()
                df_min = df.groupby(pd.Grouper(freq='4D')).min()
                df_rolling = df.rolling(24*2*4).mean()

            elif time_frame == '1m':
                df_mean = df.groupby(pd.Grouper(freq='D')).mean()
                df_max = df.groupby(pd.Grouper(freq='D')).max()
                df_min = df.groupby(pd.Grouper(freq='D')).min()
                df_rolling = df.rolling(24*2).mean()

            else:
                df_mean = df.groupby(pd.Grouper(freq='4h')).mean()
                df_max = df.loc[df.groupby(pd.Grouper(freq='4h')).idxmax().iloc[:, 0]]
                df_min = df.loc[df.groupby(pd.Grouper(freq='4h')).idxmin().iloc[:, 0]]
                df_rolling = df.rolling(8).mean()

            df_mean.columns = ['avg_mean']
            df_rolling.columns = ['rolling_mean']
            df_min.columns = ['value_min']
            df_max.columns = ['value_max']

            concat = pd.concat([df, df_max, df_min, df_mean, df_rolling], axis=1).sort_index()
            concat.fillna("null", inplace=True)

            labels = list(concat.index)
            values_avg = list(concat.avg_mean)
            values_rolling = list(concat.rolling_mean)
            values_max = list(concat.value_max)
            values_min = list(concat.value_min)
            values = list(concat.value)

            # Filter values
            #values = filter_values(values)
            if time_frame == '1y' or time_frame == '1m':
                values = []
                values_rolling = []

            else:
                values_avg = []
                values_max = []
                values_min = []

            # Last event for display
            if len(events):
                last_event = events[0]

            # Color for main graph
            if sensor.watering_trigger and sensor.watering_level and sensor.watering_level < last_event.value:
                colorFill = yellowFill
                colorLine = yellowLine
            else:
                colorFill = greenFill
                colorLine = greenLine


            # Real events and fit
            real_values = [x.real_value for x in real_events]
            real_labels = [x.value for x in real_events]
            
            if len(real_values) <= 1:
                real_labels_fit = [-2000, 2000]
            
            else:
                real_labels_fit = np.sort(np.append(max(real_labels), np.append(min(real_labels), np.random.randint(min(real_labels),max(real_labels),100))))

            real_values_fit = calibrate_raw(real_labels_fit, sensor.a0, sensor.a1, sensor.fit_type)

            if last_event:
                if not last_event.real_value:
                    last_event.real_value = "{:.2f}".format(calibrate_raw(events[0].value, sensor.a0, sensor.a1, sensor.fit_type))

            real_bubbles = list(zip(real_labels, real_values))
            real_fit = list(zip(real_labels_fit, real_values_fit))

            if sensor.watering_trigger and sensor.watering_level:
                trigger_labels = [labels[0], labels[-1]]
                trigger_values = calibrate_raw([sensor.watering_level, sensor.watering_level], sensor.a0, sensor.a1, sensor.fit_type)
                water_trigger = list(zip(trigger_labels, trigger_values))

        



    return render_template('chart.html', 
                            devices=devices,
                            sensor=sensor,
                            device=device,
                            labels=labels,
                            values=values,
                            values_avg = values_avg,
                            values_min = values_min,
                            values_max = values_max,
                            values_rolling=values_rolling,
                            real_bubbles=real_bubbles,
                            real_fit = real_fit,
                            water_trigger=water_trigger,
                            last_event=last_event,
                            colorFill=colorFill,
                            colorLine=colorLine,
                            title=device.name + " - " + sensor.name,
                            form=form,
                            sensor_form=sensor_form)