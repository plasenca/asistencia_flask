from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap5(app)
moment = Moment(app)

# Importing Routes
from routes.routes import login
