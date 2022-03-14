from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField, DecimalField, RadioField
from wtforms.validators import DataRequired, NumberRange
from connectDB import DBSingleton
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a secret'
Bootstrap(app)


def User():
    cookie = session['user']['info']
    print(f"du coté user les sessions sont{cookie}")

    if cookie[3] is True:
        title = 'formulaire'
        sql = f"SELECT * FROM Circuit"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        retourner = render_template('user.html', title=title, posts=posts)

        if request.method == 'POST':
            sql = f"SELECT Compteid FROM Compte WHERE email = '{cookie[1]}' AND mdp = '{cookie[2]}'"
            db_instance = DBSingleton.Instance()
            temp = db_instance.query(sql)
            idcompte = temp[0][0]
            print(f"les id sont {idcompte}")
            idcircuit = request.form['id']
            date = datetime.now()
            date = date.strftime("%Y-%m-%d %H:%M:%S")
            print(date)
            print(idcircuit)
            try:
                record = (idcompte, idcircuit, date)
                sql = "INSERT INTO Reservation (compteReservationID, CircuitID, dateReservation) VALUES (%s,%s,'%s')" % record
                db_instance = DBSingleton.Instance()
                db_instance.query(sql)
                print('good')
            except:
                print('pas bon')
    else:
        retourner = redirect('/')
    return retourner
