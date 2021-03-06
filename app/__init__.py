from flask import Flask
from flask_script import Manager, Command

app = Flask(__name__)
app.config.from_object('config')

manager = Manager(app)

from app.controllers import default
