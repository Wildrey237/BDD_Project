from flask import Flask, render_template, redirect, url_for, flash, request, Blueprint, make_response,session
from flask_bootstrap import Bootstrap
from auth import LogUser
from insert import addUser
from  user import User, reservation
from admin import Admin, ModifCircuit, CreateCircuit, DeleteCircuit
from admin import CreateVille, SelectVille, ModifyVille, DeleteVille
from admin import SelectCircuit , DeletePays, CreatePays, SelectPays, ModifyPays
from admin import DeleteUser, SelectUser, ModifyUser
from admin import DeleteLieu, SelectLieu, CreateLieu, ModifyLieu
from admin import DeleteEtape, SelectEtape, CreateEtape, ModifyEtape

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a secret'
Bootstrap(app)
if __name__ == '__main__':
    @app.route('/')
    def index():
        session['user'] = {"info": 'None'}
        session['circuit'] = {"id": 'None'}
        session['ville'] = {"id": 'None'}
        session['Pays'] = {"id-p": 'None'}
        return render_template('index.html')

    @app.route('/login', methods=['POST', 'GET'])
    def appeLogin():
        return LogUser()

    @app.route('/form', methods=['GET', 'POST'])
    def appelformuser():
        return addUser()

    @app.route('/user', methods=['GET', 'POST'])
    def sessionUser():
        return User()


    @app.route('/user-reservation', methods=['GET', 'POST'])
    def reservationUser():
        return reservation()

    @app.route('/admin')
    def sessionAdmin():
        return Admin()

    @app.route('/admin-circuit-modif', methods=['GET', 'POST'])
    def CircuitAdminM():
        return ModifCircuit()


    @app.route('/admin-circuit-create', methods=['GET', 'POST'])
    def CircuitAdminC():
        return CreateCircuit()


    @app.route('/admin-circuit-delete', methods=['GET', 'POST'])
    def CircuitAdminD():
        return DeleteCircuit()


    @app.route('/admin-circuit-select', methods=['GET', 'POST'])
    def CircuitAdminS():
        return SelectCircuit()

    @app.route('/admin-circuit', methods=['GET', 'POST'])
    def CircuitAdmin():
        return render_template('admin_circuit.html', title='Circuit')


    @app.route('/admin-ville-create', methods=['GET', 'POST'])
    def VilleAdminC():
        return CreateVille()


    @app.route('/admin-ville-select', methods=['GET', 'POST'])
    def VilleAdminS():
        return SelectVille()


    @app.route('/admin-ville-modify', methods=['GET', 'POST'])
    def VilleAdminM():
        return ModifyVille()


    @app.route('/admin-ville-delete', methods=['GET', 'POST'])
    def VilleAdminD():
         return DeleteVille()

    @app.route('/admin-ville', methods=['GET', 'POST'])
    def Villeadmin():
        return render_template('admin_villes.html', title='ville')


    @app.route('/admin-pays-create', methods=['GET', 'POST'])
    def PaysAdminC():
        return CreatePays()


    @app.route('/admin-pays-select', methods=['GET', 'POST'])
    def PaysAdminS():
        return SelectPays()


    @app.route('/admin-pays-modify', methods=['GET', 'POST'])
    def PaysAdminM():
        return ModifyPays()


    @app.route('/admin-pays-delete', methods=['GET', 'POST'])
    def PaysAdminD():
        return DeletePays()


    @app.route('/admin-pays', methods=['GET', 'POST'])
    def Paysadmin():
        return render_template('admin_pays.html', title='ville')


    @app.route('/admin-user-delete', methods=['GET', 'POST'])
    def UserAdminD():
        return DeleteUser()


    @app.route('/admin-user-select', methods=['GET', 'POST'])
    def UserAdminS():
        return SelectUser()


    @app.route('/admin-user-modify', methods=['GET', 'POST'])
    def UserAdminM():
        return ModifyUser()

    @app.route('/admin-user', methods=['GET', 'POST'])
    def Useradmin():
        return render_template('admin_compteclient.html', title='ville')


    """////////////////////////lieudevisite////////////////////////////"""


    @app.route('/admin-lieu-delete', methods=['GET', 'POST'])
    def LieuAdminD():
        return DeleteLieu()


    @app.route('/admin-lieu-select', methods=['GET', 'POST'])
    def LieuAdminS():
        return SelectLieu()


    @app.route('/admin-lieu-create', methods=['GET', 'POST'])
    def LieuAdminc():
        return CreateLieu()

    @app.route('/admin-lieu-modify', methods=['GET', 'POST'])
    def LieuAdminM():
        return ModifyLieu()

    @app.route('/admin-lieu', methods=['GET', 'POST'])
    def Lieuadmin():
        return render_template('admin_lieu.html', title='ville')

    """////////////////////////etape////////////////////////////"""

    @app.route('/admin-etape-delete', methods=['GET', 'POST'])
    def EtapeAdminD():
        return DeleteEtape()


    @app.route('/admin-etape-select', methods=['GET', 'POST'])
    def EtapeAdminS():
        return SelectEtape()


    @app.route('/admin-etape-create', methods=['GET', 'POST'])
    def EtapeAdminc():
        return CreateEtape()

    @app.route('/admin-etape-modify', methods=['GET', 'POST'])
    def EtapeAdminM():
        return ModifyEtape()

    @app.route('/admin-etape', methods=['GET', 'POST'])
    def Etapeadmin():
        return render_template('admin_etapes.html', title='ville')


if __name__ == '__main__':
    app.run(debug=True)