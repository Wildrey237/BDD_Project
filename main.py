from flask import Flask, render_template, redirect, url_for, flash, request, Blueprint, make_response
from flask_bootstrap import Bootstrap
from auth import LogUser
from insert import addUser
from  user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a secret'
Bootstrap(app)
if __name__ == '__main__':
    @app.route('/')
    def index():
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

    @app.route('/admin')
    def sessionAdmin():
        var = "hello sudo"
        return var

if __name__ == '__main__':
    app.run(debug=True)