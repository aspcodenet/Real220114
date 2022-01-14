from flask import Flask
from models import db
from flask_migrate import Migrate, upgrade
from random import randint

app = Flask(__name__)
app.config.from_object('config.ConfigDebug')

db.app = app
db.init_app(app)
migrate = Migrate(app,db)

@app.route("/")
def indexPage():
    tal = randint(0,10000)
    return f"<html><body><h1>Startsidan</h1><p>{tal}</p></body></html>"


@app.route("/hej")
def hejPage():
    return "<html><body><h1>Hej hej</h1></body></html>"

@app.route("/hopp")
def hoppPage():
    return "<html><body><h1>Hopp</h1></body></html>"


if __name__  == "__main__":
    with app.app_context():
        upgrade()
    app.run()


