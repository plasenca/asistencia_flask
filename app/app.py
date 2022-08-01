from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from flask_moment import Moment
from flask_migrate import Migrate
from config import config

# App initialization
app = Flask(__name__)
# Setting configuration
app.config.from_object(config["development"])

# Incializa el login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Bootstrap initialization
bootstrap = Bootstrap5()
bootstrap.init_app(app)

# Moment initialization
moment = Moment()
moment.init_app(app)

# SQLAlchemy initialization
db = SQLAlchemy()
db.init_app(app)

# Migrate initialization
migrate = Migrate(app, db)

# Importing Routes
from routes.routes import *