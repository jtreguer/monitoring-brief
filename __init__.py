from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from datetime import datetime
from os import getenv
from .auxiliary import Auxiliary
import logging



def create_app(env: str='dev'):
    app = Flask(__name__)
    print(env)
    app.config.update(use_reloader=False)

    return app