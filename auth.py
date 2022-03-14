from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField, DecimalField, PasswordField, \
    EmailField
from wtforms.validators import DataRequired, NumberRange
from connectDB import DBSingleton

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a secret'
Bootstrap(app)


class authform(FlaskForm):
    mail = EmailField('mail', validators=[DataRequired()])
    MDP = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Submit')
    session_MAIL = None
    Session_MDP = None
    Session_id = None


def log():
    form = authform()
    cookie = False
    retourner = [None, None, None, cookie]
    if form.validate_on_submit():
        mail = request.form.get('mail')
        MDP = request.form.get('MDP')
        sql = f"SELECT email FROM Compte WHERE email = '{mail}'"
        db_instance = DBSingleton.Instance()
        temp = db_instance.query(sql)
        if len(temp) == 0:
            print('vide')
        else:
            true_mail = temp[0][0]
            if true_mail == mail:
                sql = f"SELECT mdp FROM Compte WHERE email = '{mail}'"
                db_instance = DBSingleton.Instance()
                temp = db_instance.query(sql)
                password = temp[0][0]
                """mot de passe prit part le insert"""
                if password == MDP:
                    sql = f"SELECT role FROM Compte WHERE email = '{mail}' AND mdp = '{MDP}'"
                    db_instance = DBSingleton.Instance()
                    temp = db_instance.query(sql)
                    role = temp[0][0]
                    cookie = True
                    retourner = [role, mail, MDP, cookie]
                    session['user'] = {"info": retourner}
                    print(f"le mot de passe session est {retourner}")
                else:
                    print("pas bon mdp")
    return retourner

def LogUser():
    cookie = log()
    form = authform()
    role = cookie[0]
    print(cookie)
    session['user'] = {"info": cookie}
    print(session['user']['info'])
    title = 'login'
    result = render_template('user-connect.html', form=form, title=title)
    if cookie[3] is True:
        if role == 1:
            result = redirect('/admin')
        elif role == 0:
            result = redirect('/user')
    return result


if __name__ == '__main__':
    app.run(debug=True)
