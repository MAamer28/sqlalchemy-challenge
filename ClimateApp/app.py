# Import the dependencies.
from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

# reflect the tables

Base.prepare(autoload_with = engine)

# Save references to each table

measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    return """ <h1> Climate API - Hawaii </h1> 
    <h3> Available API Routes: </h3>
    <ul>
        <li><a href = "/api/v1.0/precipitation"> Precipitation </a> </li>
        <li><a href = "/api/v1.0/stations"> Stations </a> </li>
        <li><a href = "/api/v1.0/tobs"> Temperature </a></li>
    </ul>
        """

@app.route("/api/v1.0/precipitation")
def precipitation():
    end_date = session.query(func.max(measurement.date)).first()[0]
    start_date = dt.datetime.strptime(end_date, "%Y-%m-%d") - dt.timedelta(days = 365)
    yearly_prcp = session.query(measurement.date, measurement.prcp).filter(measurement.date >= start_date()).all()

    list_prcp = []
    for date, prcp in yearly_prcp:
        dict_prcp = {}
        dict_prcp["date"] = date
        dict_prcp["prcp"] = prcp
        list_prcp.append(dict_prcp)
    
    return jsonify(list_prcp)

@app.route("/api/v1.0/stations")
def stations():
    station_info = session.query(station.station).all()
    
    list_stations = list(np.ravel(station_info))

    return jsonify(list_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    end_date = session.query(func.max(measurement.date)).first()[0]
    start_date = dt.datetime.strptime(end_date, "%Y-%m-%d") - dt.timedelta(days = 365)

    tobs_data = session.query(measurement.date, measurement.tobs).filter(measurement.station == 'USC00519281').filter(measurement.date >= start_date).all()

    list_tobs = []
    for date, tobs in tobs_data:
        dict_tobs = {}
        dict_tobs["date"] = date
        dict_tobs["tobs"] = tobs
        list_tobs.append(dict_tobs)
    
    return jsonify(list_tobs)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temp_info(start = None, end = None):
    sel = [func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)]

    if end == None:
        info_start = session.query(*sel).filter(measurement.date >= start).all()

        list_start = list(np.ravel(info_start))

        return jsonify(list_start)
    
    else:
        period_data = session.query(*sel).filter(measurement.date >= start).filter(measurement.date <= end).all()
        list_period = list(np.ravel(period_data))

        return jsonify(list_period)

session.close()

if __name__ == "__main__":
    app.run(debug = True)