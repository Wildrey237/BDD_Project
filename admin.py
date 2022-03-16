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


def Admin():
    cookie = session['user']['info']
    print(f"les cookies du admin sont{cookie}")
    if cookie[0] == 1 and cookie[3] is True:
        title = 'admin'
        retourner = render_template('admin.html', title=title, posts='Bonjour admin' )
    else:
        retourner = redirect('/')
    return retourner
