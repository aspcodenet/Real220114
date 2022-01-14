from flask import Flask
from models import db
from flask_migrate import Migrate, upgrade


app = Flask(__name__)
app.config.from_object('config.ConfigDebug')
#app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+mysqlconnector://root:password@localhost/inlamning'    # File-based SQL database

db.app = app
db.init_app(app)
migrate = Migrate(app,db)

if __name__  == "__main__":
    with app.app_context():
        upgrade()
    app.run()


