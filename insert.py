from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField, DecimalField,  DateField
from wtforms.validators import DataRequired, NumberRange
from connectDB import DBSingleton

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a secret'
Bootstrap(app)


class InsertUserForm(FlaskForm):
    name = StringField('nom', validators=[DataRequired()])
    surname = StringField('prenom', validators=[DataRequired()])
    mail = StringField('mail', validators=[DataRequired()])
    date = DateField('Date' ,format ='%Y-%m-%d')
    MDP = StringField('mot de passe ?')
    role = SelectField('Quel est son role', choices=['admin','user'])
    submit = SubmitField('Submit')

def addUser():
    form = InsertUserForm()
    retourner = render_template('titanic.html', form=form)
    if form.validate_on_submit():
        nom = form.name.data
        prenom = form.surname.data
        mdp = form.MDP.data
        mail = form.mail.data
        buffday = request.form['date']
        buffday = str(buffday)
        print(buffday)
        role = form.role.data
        if role == 'admin':
            role = 1
        else:
            role = 0
        if not mail:
            flash('Title is required!')
        else:
            record = (nom, prenom, mdp, mail, buffday, role)
            sql = "INSERT INTO Compte ( nom, prenom, mdp, email, DateDeNaissance, role) VALUES ('%s','%s','%s','%s','%s',%s);" % record
            db_instance = DBSingleton.Instance()
            db_instance.query(sql)
            retourner = redirect('/connect')
    return retourner

if __name__ == '__main__':
    app.run(debug=True)