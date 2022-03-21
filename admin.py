from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField, DecimalField, RadioField, \
    DateField, TextAreaField
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
        retourner = render_template('admin.html', title=title, posts='Bonjour admin')
    else:
        retourner = redirect('/')
    return retourner


def CreateCircuit():
    cookie = session['user']['info']
    title = 'Circuit'
    if cookie[0] == 1 and cookie[3] is True:
        sql = "SELECT villeID, nom FROM Ville"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        tailles = ""
        retourner = render_template('admin_circuit.html', title=title, posts=posts, taille=tailles, nom='Modify')

        if request.method == 'POST':
            descriptif = request.form['descriptif']
            datedepart = request.form['dateDepart']
            nbre_p = request.form['nbrPlacesDisponibles']
            duree = request.form['dureeEnJours']
            prix = request.form['prixInscription']
            id_depart = request.form['villeDepartID']
            id_arrive = request.form['villeArriveeID']
            record = (descriptif, datedepart, nbre_p, duree, prix, id_depart, id_arrive)
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

def is_user_logged():
    cookie = session['user']['info']
    return cookie[0] == 1 and cookie[3] is True

def SelectCircuit():
    title = 'Circuit'
    if is_user_logged():
        sql = "SELECT * FROM Circuit"
        db_instance = DBSingleton.Instance()
        taille = db_instance.query(sql)
        retourner = render_template('admin_circuit.html', title=title, tailles=taille, nom="select-Modify")
        if request.method == "POST":
            id = request.form['id-circuit']
            session['circuit'] = {"id": id}
            retourner = redirect('/admin-circuit-modif')
    else:
        retourner = redirect('/')
    return retourner

def ModifCircuit():
    title = 'Circuit'
    idcircuit = session['circuit']['id']
    print(idcircuit)
    if is_user_logged():
        sql = "SELECT villeID, nom FROM Ville"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)

        sql = f"SELECT * FROM Circuit WHERE ID = {idcircuit}"
        print(sql)
        db_instance = DBSingleton.Instance()
        tailles = db_instance.query(sql)
        print(tailles)

        retourner = render_template('admin_circuit.html', title=title, posts=posts, taille=tailles[0], nom='Modify')
        if request.method == 'POST':
            descriptif = request.form['descriptif']
            datedepart = request.form['dateDepart']
            NbreP = request.form['nbrPlacesDisponibles']
            duree = request.form['dureeEnJours']
            prix = request.form['prixInscription']
            idDepart = request.form['villeDepartID']
            idArrive = request.form['villeArriveeID']

            try:
                sql = f"""UPDATE Circuit 
                SET descriptif = '{descriptif}', 
                dateDepart = '{datedepart}', 
                nbrPlacesDisponibles = {NbreP}, 
                dureeEnJours = {duree}, 
                prixInscription = {prix}, 
                villeDepartID = {idDepart}, 
                villeArriveeID = {idArrive} 
                WHERE Circuit.ID = {idcircuit};"""
                db_instance = DBSingleton.Instance()
                db_instance.query(sql)
                print("good")
            except:
                print("faux")
    else:
        retourner = redirect('/')
    return (retourner)


def DeleteCircuit():
    cookie = session['user']['info']
    title = 'Circuit'
    if cookie[0] == 1 and cookie[3] is True:
        sql = """SELECT Circuit.ID,Circuit.descriptif, Circuit.dateDepart, Circuit.nbrPlacesDisponibles, Circuit.dureeEnJours, Circuit.prixInscription, Media.images, Pays.paysID, Pays.nom
                 FROM Circuit
                 JOIN Etape ON Circuit.ID = Etape.Circuit_ID
                 JOIN LieuDeVisite ON Etape.LieuDeVisite_ID = LieuDeVisite.ID
                 JOIN Media ON LieuDeVisite.ID = Media.LieuDeVisite_ID
                 JOIN Ville ON Ville.villeID = Circuit.villeDepartID
                 JOIN Pays ON Pays.paysID = Ville.Pays_paysID"""
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        if request.method == 'POST':
            idcircuit = request.form['id']
            sql = f"DELETE FROM Circuit WHERE Circuit.ID = {idcircuit}"
            print(sql)
            db_instance = DBSingleton.Instance()
            db_instance.query(sql)
            posts = 'Suppresion reussi'
        retourner = render_template('admin_circuit.html', title=title, posts=posts, nom ="Delete")
    return retourner

def CreateVille():
    cookie = session['user']['info']
    title = 'Circuit'
    if cookie[0] == 1 and cookie[3] is True:
        sql = "SELECT * FROM Pays"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        retourner = render_template('admin_villes.html', title=title, posts=posts, name='Modify')

        if request.method == 'POST':
            nom_ville = request.form['nom']
            id_pays = request.form['Pays_paysID']
            record = (nom_ville, id_pays)
            print(record)
            try:
                sql = """INSERT INTO Circuit (nom, Pays_paysID) 
                    VALUES ('%s', %s);""" % (nom_ville, id_pays)
                db_instance = DBSingleton.Instance()
                db_instance.query(sql)
                print('good')
            except:
                print('pas bon')
    else:
        retourner = redirect('/')
    return (retourner)