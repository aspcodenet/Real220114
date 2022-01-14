from flask import Flask, render_template
from models import db, Person
from flask_migrate import Migrate, upgrade
from random import randint

app = Flask(__name__)
app.config.from_object('config.ConfigDebug')

db.app = app
db.init_app(app)
migrate = Migrate(app,db)

@app.route("/")
def indexPage():
    allaPersoner = Person.query.all()
    return render_template('startPage.html', allaPersoner=allaPersoner)

@app.route("/hej")
def hejPage():
    return render_template('hej.html')

@app.route("/hopp")
def hoppPage():
    return "<html><body><h1>Hopp</h1></body></html>"


if __name__  == "__main__":
    with app.app_context():
        upgrade()
    app.run()


