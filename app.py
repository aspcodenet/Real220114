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
    #antalPersoner = Person count???
    #totSaldo = 
    return render_template('startPage.html', allaPersoner=allaPersoner, antalPersoner=12, totSaldo=999)

@app.route("/person/<id>")
def personPage(id):
    person = Person.query.filter(Person.id == id).first()
    return render_template('person.html', person=person)

@app.route("/hopp")
def hoppPage():
    return "<html><body><h1>Hopp</h1></body></html>"


if __name__  == "__main__":
    with app.app_context():
        upgrade()
    app.run()


