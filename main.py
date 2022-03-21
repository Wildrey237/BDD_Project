from flask import Flask, render_template, redirect, url_for, flash, request, Blueprint, make_response,session
from flask_bootstrap import Bootstrap
from auth import LogUser
from insert import addUser
from  user import User, reservation
from admin import Admin, ModifCircuit, CreateCircuit, DeleteCircuit, SelectCircuit, CreateVille

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a secret'
Bootstrap(app)
if __name__ == '__main__':
    @app.route('/')
    def index():
        session['user'] = {"info": 'None'}
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

if __name__ == '__main__':
    app.run(debug=True)