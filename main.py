from flask import Flask, render_template, redirect, url_for, flash, request, Blueprint
from flask_bootstrap import Bootstrap
from connectDB import DBSingleton
app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a secret'
Bootstrap(app)

if __name__ == '__main__':
    @app.route('/')
    def index():
        render_template('titanic.html')

    @app.route('/profile')
    def profile():
        return render_template('profile.html')


    """auth"""
    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/signup')
    def signup():
        return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)