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
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

# reflect the tables
Base.prepare(autoload_with = engine)

# Save references to each table

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
