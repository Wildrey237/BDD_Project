from flask import Flask, render_template, redirect, url_for, flash, request, Blueprint
from flask_bootstrap import Bootstrap
from auth import login
from insert import addUser

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a secret'
Bootstrap(app)

if __name__ == '__main__':

    @app.route('/titanic/connect', methods=['POST', 'GET'])
    def appeLogin():
        return  login()

    @app.route('/titanic/user')
    def sessionUser():
        return ("hello user")


    @app.route('/titanic/admin')
    def sessionAdmin():
        return ("hello sudo")

    @app.route('/titanic/correct')
    def temp():
        return ("hello")


    @app.route('/titanic/adduser', methods=['GET', 'POST'])
    def appelformuser():
        return addUser()


if __name__ == '__main__':
    app.run(debug=True)