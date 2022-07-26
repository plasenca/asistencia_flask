from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from flask_moment import Moment

app = Flask(__name__)
app.secret_key = 'superduper secret string'
# Incializa el login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Configura bootstrap
bootstrap = Bootstrap5(app)

# Configura moment
moment = Moment(app)

# Importing Routes
from routes.routes import *
