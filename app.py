from flask import Flask
from models import db
from flask_migrate import Migrate, upgrade


app = Flask(__name__)
app.config.from_object(__name__ + '.ConfigDebug')

#db.app = app
db.init_app(app)


