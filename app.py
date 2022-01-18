from flask import Flask, render_template, request
from models import db, Person
from flask_migrate import Migrate, upgrade
from random import randint

app = Flask(__name__)
app.config.from_object('config.ConfigDebug')

db.app = app
db.init_app(app)
migrate = Migrate(app,db)

@app.route("/hej")
def hejPage():
    # på riktigt kolla om inloggad osv sov
    lista = ["Stefan", "Oliver", "Josefine"]
    return render_template('hej.html', inloggad=True, lista=lista,age=49, name="Stefan")



@app.route("/")
def indexPage():
    activePage = "startPage"
    allaPersoner = Person.query.all()
    #antalPersoner = Person count???
    #totSaldo = 
    return render_template('startPage.html', antalPersoner=12, totSaldo=999,activePage=activePage)


@app.route("/personer")
def personerPage():
    
    sortColumn = request.args.get('sortColumn')
    sortOrder = request.args.get('sortOrder')

    if sortColumn == "" or sortColumn == None:
        sortColumn = "namn"

    if sortOrder == "" or sortOrder == None:
        sortOrder = "asc"

    activePage = "personerPage"
    allaPersoner = Person.query

    if sortColumn == "namn":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Person.namn.desc())
        else:
            allaPersoner = allaPersoner.order_by(Person.namn.asc())

    if sortColumn == "city":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Person.city.desc())
        else:
            allaPersoner = allaPersoner.order_by(Person.city.asc())

    if sortColumn == "postal":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Person.postalcode.desc())
        else:
            allaPersoner = allaPersoner.order_by(Person.postalcode.asc())

    return render_template('personer.html', allaPersoner=allaPersoner, activePage=activePage)


@app.route("/person/<id>")
def personPage(id):
    person = Person.query.filter(Person.id == id).first()
    return render_template('person.html',person=person, name="Stefan")



@app.route("/hopp")
def hoppPage():
    return "<html><body><h1>Hopp</h1></body></html>"


if __name__  == "__main__":
    with app.app_context():
        upgrade()
    app.run()


