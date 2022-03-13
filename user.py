from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField, DecimalField, RadioField
from wtforms.validators import DataRequired, NumberRange
from connectDB import DBSingleton

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a secret'
Bootstrap(app)


def User():
    title = 'formulaire'
    sql = f"SELECT * FROM Circuit"
    db_instance = DBSingleton.Instance()
    posts = db_instance.query(sql)
    retourner = render_template('user.html', title=title, posts=posts)
    if request.method == 'POST':
        id = request.form['id']
        print(id)
    return retourner
