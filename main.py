from flask import Flask, render_template, redirect, url_for, flash, request, Blueprint
from flask_bootstrap import Bootstrap
from auth import log, testlog
from insert import addUser

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a secret'
Bootstrap(app)
if __name__ == '__main__':
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/connect', methods=['POST', 'GET'])
    def appeLogin():
        return  log()

    @app.route('/form', methods=['GET', 'POST'])
    def appelformuser():
        return addUser()

    @app.route('/user')
    def sessionUser():
        session = testlog()
        boolean = session[3]
        role = session[0]
        if boolean == False:
            var = redirect("/")
        else:
            if role == 0:
                var = "hello user"
        return var

    @app.route('/admin')
    def sessionAdmin():
        session = testlog()
        boolean = session[3]
        role = session[0]
        if boolean == False:
            var = redirect("/")
        else:
            if role == 0:
                var = "hello sudo"
        return var

if __name__ == '__main__':
    app.run(debug=True)