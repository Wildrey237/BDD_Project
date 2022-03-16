from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField, DecimalField, RadioField, DateField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
from connectDB import DBSingleton
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a secret'
Bootstrap(app)


def Admin():
    cookie = session['user']['info']
    print(f"les cookies du admin sont{cookie}")
    if cookie[0] == 1 and cookie[3] is True:
        title = 'admin'
        retourner = render_template('admin.html', title=title, posts='Bonjour admin' )
    else:
        retourner = redirect('/')
    return retourner

def ModifCircuit():
    cookie = session['user']['info']
    title = 'Circuit'
    if cookie[0] == 1 and cookie[3] is True:
        sql = "SELECT villeID, nom FROM Ville"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        retourner = render_template('admin_circuit.html', title=title, posts=posts)

        if request.method == 'POST':
            descriptif = request.form['descriptif']
            datedepart = request.form['dateDepart']
            NbreP = request.form['nbrPlacesDisponibles']
            duree = request.form['dureeEnJours']
            prix = request.form['prixInscription']
            idDepart = request.form['villeDepartID']
            idA = request.form['villeArriveeID']
            record = (descriptif, datedepart, NbreP, duree, prix, idDepart, idA)
            print(record)
            try:
                sql = """INSERT INTO Circuit (descriptif, dateDepart, nbrPlacesDisponibles, dureeEnJours, prixInscription, villeDepartID, villeArriveeID) 
                VALUES ('%s', '%s', %s, %s, %s, %s, %s);""" % record
                db_instance = DBSingleton.Instance()
                db_instance.query(sql)
                print('good')
            except:
                print('pas bon')
    else:
        retourner = redirect('/')
    return (retourner)