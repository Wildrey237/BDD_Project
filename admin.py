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


def is_user_logged():
    cookie = session['user']['info']
    is_admin = 1
    return cookie[0] == is_admin and cookie[3] is True


def Admin():
    cookie = session['user']['info']
    print(f"les cookies du admin sont{cookie}")
    if is_user_logged():
        title = 'admin'
        retourner = render_template('admin.html', title=title, posts='')
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
                retourner = redirect("/admin-circuit")
            except:
                print('pas bon')
    else:
        retourner = redirect('/')
    return retourner


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
        if idcircuit == 'None':
            retourner = redirect("/admin-circuit-select")
        else:
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
                    retourner = redirect("/admin-circuit")
                except:
                    print("faux")
    else:
        retourner = redirect('/')
    return retourner


def DeleteCircuit():
    title = 'Circuit'
    if is_user_logged():
        sql = """SELECT Circuit.ID,Circuit.descriptif, Circuit.dateDepart, Circuit.nbrPlacesDisponibles, Circuit.dureeEnJours, Circuit.prixInscription, Media.images, Pays.paysID, Pays.nom
                 FROM Circuit
                 JOIN Etape ON Circuit.ID = Etape.Circuit_ID
                 JOIN LieuDeVisite ON Etape.LieuDeVisite_ID = LieuDeVisite.ID
                 JOIN Media ON LieuDeVisite.ID = Media.LieuDeVisite_ID
                 JOIN Ville ON Ville.villeID = Circuit.villeDepartID
                 JOIN Pays ON Pays.paysID = Ville.Pays_paysID"""
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        retourner = render_template('admin_circuit.html', title=title, posts=posts, nom="Delete")
        if request.method == 'POST':
            idcircuit = request.form['id']
            sql = f"DELETE FROM Circuit WHERE Circuit.ID = {idcircuit}"
            print(sql)
            db_instance = DBSingleton.Instance()
            db_instance.query(sql)
            retourner = redirect("/admin-circuit")
    return retourner


def CreateVille():
    title = 'Circuit'
    if is_user_logged():
        sql = "SELECT * FROM Pays"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        retourner = render_template('admin_villes.html', title=title, posts=posts, tailles="", nom='creer')

        if request.method == 'POST':
            nom_ville = request.form['nom']
            id_pays = request.form['id-pays']
            id_pays = int(id_pays)
            record = (nom_ville, id_pays)
            print(record)
            try:
                sql = "INSERT INTO Ville (nom, Pays_paysID) VALUES ('%s', '%s');" % record
                db_instance = DBSingleton.Instance()
                db_instance.query(sql)
                print('good')
                retourner = redirect('/admin-ville')
            except:
                print('pas bon')
    else:
        retourner = redirect('/')
    return retourner


def SelectVille():
    title = 'Circuit'
    if is_user_logged():
        sql = "SELECT * FROM Ville"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        retourner = render_template('admin_villes.html', title=title, posts=posts, nom='select-ville')
        if request.method == "POST":
            id = request.form['id-circuit']
            print(id)
            session['ville'] = {"id": id}
            retourner = redirect('/admin-ville-modify')
    else:
        retourner = redirect('/')
    return retourner


def ModifyVille():
    title = 'Circuit'
    id = session['ville']['id']
    print(f'ici {id}')
    if is_user_logged():
        sql = f"SELECT * FROM Ville WHERE villeID = {id}"
        db_instance = DBSingleton.Instance()
        taille = db_instance.query(sql)

        sql = "SELECT * FROM Pays"
        db_instance = DBSingleton.Instance()
        post = db_instance.query(sql)

        retourner = render_template('admin_villes.html', title=title, posts=post, tailles=taille[0], nom='creer')
        idville = session['ville']['id']
        if request.method == 'POST':
            nom_ville = request.form['nom']
            id_pays = request.form['id-pays']
            id_pays = int(id_pays)
            record = (nom_ville, id_pays)
            print(record)

            try:
                sql = f"UPDATE Ville SET nom = '{nom_ville}', Pays_paysID = {id_pays} WHERE Ville.villeID = {idville};"
                print(sql)
                db_instance = DBSingleton.Instance()
                db_instance.query(sql)
                print('good')
                retourner = redirect('/admin-ville')
            except:
                print('pas bon')
    else:
        retourner = redirect('/')
    return retourner


def DeleteVille():
    title = 'Ville'
    if is_user_logged():
        sql = "SELECT * FROM Ville"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        retourner = render_template('admin_villes.html', title=title, posts=posts, nom='delete')
        if request.method == "POST":
            id = request.form['id-circuit']
            sql = f"DELETE FROM Ville WHERE Ville.villeID =  {id}"
            print(sql)
            db_instance = DBSingleton.Instance()
            db_instance.query(sql)
            print('bon')
            retourner = redirect('/admin-ville')
    else:
        retourner = redirect('/')
    return retourner


"""/////////////////////// Pays/////////////////////////////"""


def CreatePays():
    title = 'Pays'
    if is_user_logged():
        retourner = render_template('admin_pays.html', title=title, tailles=" ", nom='creer')
        if request.method == 'POST':
            nom_pays = request.form['nom']
            try:
                sql = f"INSERT INTO Pays (nom) VALUES ('{nom_pays}');"
                db_instance = DBSingleton.Instance()
                db_instance.query(sql)
                print('good')
                retourner = redirect('/admin-pays')
            except:
                print('pas bon')
    else:
        retourner = redirect('/')
    return retourner


def SelectPays():
    title = 'Circuit'
    if is_user_logged():
        sql = "SELECT * FROM Pays"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        retourner = render_template('admin_pays.html', title=title, posts=posts, nom='select')
        if request.method == "POST":
            id = request.form['id-circuit']
            print(id)
            session['Pays'] = {'id-p': id}
            print(session['Pays'])
            retourner = redirect('/admin-pays-modify')
    else:
        retourner = redirect('/')
    return retourner


def ModifyPays():
    title = 'Circuit'
    print(f"les cookies {session['Pays']}")
    id_pays = session['Pays']['id-p']
    print(f'ici {id_pays}')
    if is_user_logged():
        sql = f"SELECT * FROM Pays WHERE paysID = {id_pays}"
        db_instance = DBSingleton.Instance()
        taille = db_instance.query(sql)
        retourner = render_template('admin_pays.html', title=title, tailles=taille[0], nom='creer')
        if request.method == 'POST':
            nom_pays = request.form['nom']
            id_pays = int(id_pays)

            try:
                sql = f"UPDATE Pays SET nom = '{nom_pays}' WHERE Pays.paysID = {id_pays};"
                print(sql)
                db_instance = DBSingleton.Instance()
                db_instance.query(sql)
                print('good')
                retourner = redirect('/admin-pays')
            except:
                print('pas bon')
    else:
        retourner = redirect('/')
    return retourner


def DeletePays():
    title = 'Pays'
    if is_user_logged():
        sql = "SELECT * FROM Pays"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        retourner = render_template('admin_pays.html', title=title, posts=posts, nom='delete')
        if request.method == "POST":
            id = request.form['id-circuit']
            sql = f"DELETE FROM Pays WHERE Pays.paysID = {id}"
            print(sql)
            db_instance = DBSingleton.Instance()
            db_instance.query(sql)
            print('bon')
            retourner = redirect('/admin-pays')
    else:
        retourner = redirect('/')
    return retourner


"""/////////////////compte user////////////////////////"""


def SelectUser():
    title = 'User'
    if is_user_logged():
        sql = "SELECT * FROM Compte"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        retourner = render_template('admin_compteclient.html', title=title, posts=posts, nom='select')
        if request.method == "POST":
            id = request.form['id-client']
            print(id)
            session['User'] = {'id-u': id}
            print(session['Pays'])
            retourner = redirect('/admin-user-modify')
    else:
        retourner = redirect('/')
    return retourner


def ModifyUser():
    title = 'Circuit'
    id_compte = session['User']['id-u']
    print(f'ici {id_compte}')
    if is_user_logged():
        sql = f"SELECT * FROM Compte WHERE compteID = {id_compte}"
        db_instance = DBSingleton.Instance()
        taille = db_instance.query(sql)
        retourner = render_template('admin_compteclient.html', title=title, taille=taille[0], nom='creer')
        if request.method == 'POST':
            nom_user = request.form['nom']
            prenom_user = request.form['prenom']
            mdp = request.form['mdp']
            date = request.form['DateDeNaissance']
            role = request.form['role']
            email = request.form['email']
            id_compte = int(id_compte)

            try:
                sql = f"""UPDATE Compte SET nom = '{nom_user}', 
                                            prenom = '{prenom_user}', 
                                            `mdp` = '{mdp}', 
                                            `DateDeNaissance` = '{date}', 
                                            `role` = '{role}', 
                                            `email` = '{email}' 
                        WHERE `Compte`.`compteID` = {id_compte}"""
                print(sql)
                db_instance = DBSingleton.Instance()
                db_instance.query(sql)
                print('good')
                retourner = redirect('/admin-user')
            except:
                print('pas bon')
    else:
        retourner = redirect('/')
    return retourner


def DeleteUser():
    title = 'User'
    if is_user_logged():
        sql = "SELECT * FROM Compte"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        retourner = render_template('admin_compteclient.html', title=title, posts=posts, nom='delete')
        if request.method == "POST":
            id = request.form['id-circuit']
            sql = f"DELETE FROM Compte WHERE Compte.compteID = {id}"
            print(sql)
            db_instance = DBSingleton.Instance()
            db_instance.query(sql)
            print('bon')
            retourner = redirect('/admin-user')
    else:
        retourner = redirect('/')
    return retourner


"""///////////////// lieu ////////////////////////"""

def CreateLieu():
    title = 'Pays'
    if is_user_logged():
        sql = "SELECT * FROM Ville"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        retourner = render_template('admin_lieu.html', title=title, tailles=" ", posts=posts, nom='creer')
        if request.method == 'POST':
            label = request.form['label']
            des = request.form['descriptif']
            prix = request.form['prixVisite']
            villeid = request.form['Ville_villeID']
            record = (label, des, prix, villeid)
            try:
                sql = """INSERT INTO LieuDeVisite (label, descriptif, prixVisite, Ville_villeID) 
                         VALUES ('%s', '%s', '%s', '%s')""" % record
                db_instance = DBSingleton.Instance()
                db_instance.query(sql)
                print('good')
                retourner = redirect('/admin-lieu')
            except:
                print('pas bon')
    else:
        retourner = redirect('/')
    return retourner


def SelectLieu():
    title = 'Circuit'
    if is_user_logged():
        sql = "SELECT * FROM LieuDeVisite"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        retourner = render_template('admin_lieu.html', title=title, posts=posts, nom='select')
        if request.method == "POST":
            id = request.form['id-circuit']
            print(id)
            session['lieu'] = {'id-l': id}
            retourner = redirect('/admin-lieu-modify')
    else:
        retourner = redirect('/')
    return retourner


def ModifyLieu():
    title = 'Circuit'
    id_lieu = session['lieu']['id-l']
    if is_user_logged():
        sql = f"SELECT * FROM LieuDeVisite WHERE ID = {id_lieu}"
        db_instance = DBSingleton.Instance()
        taille = db_instance.query(sql)

        sql = "SELECT * FROM Ville"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)

        retourner = render_template('admin_lieu.html', title=title, tailles=taille[0], posts=posts, nom='creer')
        if request.method == 'POST':
            label = request.form['label']
            des = request.form['descriptif']
            prix = request.form['prixVisite']
            villeid = request.form['Ville_villeID']
            id_lieu = int(id_lieu)

            try:
                sql = f"""UPDATE `LieuDeVisite` 
                          SET label = '{label}', 
                              descriptif = '{des}', 
                              prixVisite = '{prix}', 
                              Ville_villeID = '{villeid}' 
                          WHERE LieuDeVisite.ID = {id_lieu};"""
                print(sql)
                db_instance = DBSingleton.Instance()
                db_instance.query(sql)
                print('good')
                retourner = redirect('/admin-lieu')
            except:
                print('pas bon')
    else:
        retourner = redirect('/')
    return retourner


def DeleteLieu():
    title = 'Pays'
    if is_user_logged():
        sql = "SELECT * FROM LieuDeVisite"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        retourner = render_template('admin_lieu.html', title=title, posts=posts, nom='delete')
        if request.method == "POST":
            id = request.form['id-circuit']
            sql = f"DELETE FROM LieuDeVisite WHERE LieuDeVisite.ID = {id}"
            print(sql)
            db_instance = DBSingleton.Instance()
            db_instance.query(sql)
            print('bon')
            retourner = redirect('/admin-lieu')
    else:
        retourner = redirect('/')
    return retourner


"""///////////////// Etape ////////////////////////"""

def CreateEtape():
    title = 'Pays'
    if is_user_logged():
        sql = "SELECT * FROM Circuit"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)

        sql = "SELECT * FROM Ville"
        db_instance = DBSingleton.Instance()
        villes = db_instance.query(sql)

        retourner = render_template('admin_etapes.html', places=" ",title=title, tailles=" ", posts=posts, Villes=villes, nom='creer')
        if request.method == 'POST':
            ordre = request.form['ordre']
            date = request.form['dateEtape']
            duree = request.form['dureeEnMinutes']
            id_circuit = request.form['id-circuit']
            villeid = request.form['id-lieux']
            record = (ordre, date, duree, id_circuit, villeid)
            try:
                sql = """INSERT INTO Etape (ordre, dateEtape, dureeEnMinute, circuit_ID, LieuDeVisite_ID)
                         VALUES ('%s', '%s', '%s', '%s', '%s')""" % record
                db_instance = DBSingleton.Instance()
                db_instance.query(sql)
                print('good')
            except:
                print('pas bon')
    else:
        retourner = redirect('/')
    return retourner


def SelectEtape():
    title = 'Circuit'
    if is_user_logged():
        sql = "SELECT * FROM Etape"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        retourner = render_template('admin_etapes.html', title=title, posts=posts, nom='select')
        if request.method == "POST":
            role = request.form['id-circuit']
            print(role)
            session['etape'] = {'role': role}
            retourner = redirect('/admin-etape-modify')
    else:
        retourner = redirect('/')
    return retourner


def ModifyEtape():
    title = 'Circuit'
    role = session['etape']['role']
    if is_user_logged():
        sql = f"SELECT * FROM Etape WHERE ordre = {role}"
        db_instance = DBSingleton.Instance()
        taille = db_instance.query(sql)

        sql = "SELECT * FROM Circuit"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)

        temp = {"ordre":taille[0][0],
                "circuit": taille[0][2],
                "lieu": taille[0][3]}
        sql = "SELECT * FROM Ville"
        db_instance = DBSingleton.Instance()
        villes = db_instance.query(sql)

        sql = "SELECT * FROM Etape"
        db_instance = DBSingleton.Instance()
        places = db_instance.query(sql)

        retourner = render_template('admin_etapes.html', title=title, places=places[0], tailles=taille, posts=posts, Villes=villes, nom='creer')
        if request.method == 'POST':
            ordre = request.form['ordre']
            date = request.form['dateEtape']
            duree = request.form['dureeEnMinutes']
            id_circuit = request.form['id-circuit']
            villeid = request.form['id-lieux']

            try:
                sql = f"""UPDATE Etape 
                          SET ordre = '{ordre}', 
                          dateEtape = '{date}', 
                          dureeEnMinute = '{duree}', 
                          circuit_ID = '{id_circuit}', 
                          LieuDeVisite_ID = '{villeid}' 
                          WHERE Etape.ordre = {temp["ordre"]} 
                          AND Etape.circuit_ID = {temp["circuit"]} 
                          AND Etape.LieuDeVisite_ID = {temp["lieu"]};"""
                print(sql)
                db_instance = DBSingleton.Instance()
                db_instance.query(sql)
                print('good')
                retourner = redirect('/admin-etape')
            except:
                print('pas bon')
    else:
        retourner = redirect('/')
    return retourner


def DeleteEtape():
    title = 'Pays'
    if is_user_logged():
        sql = "SELECT * FROM Etape"
        db_instance = DBSingleton.Instance()
        posts = db_instance.query(sql)
        retourner = render_template('admin_etapes.html', title=title, posts=posts, nom='delete')
        if request.method == "POST":
            id = request.form['id-circuit']
            sql = f"DELETE FROM Etape WHERE Etape.ordre = {id}"
            print(sql)
            db_instance = DBSingleton.Instance()
            db_instance.query(sql)
            print('bon')
            retourner = redirect('/admin-etape')
    else:
        retourner = redirect('/')
    return retourner