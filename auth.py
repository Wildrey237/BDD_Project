from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField, DecimalField
from wtforms.validators import DataRequired, NumberRange
from connectDB import DBSingleton

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a secret'
Bootstrap(app)

class authform(FlaskForm):
    mail = StringField('mail', validators=[DataRequired()])
    MDP = StringField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Submit')
    session_MAIL = None
    Session_MDP = None
    Session_id = None
def testlog():
    form = authform()
    boolean = 0
    retourner = ['non', 'non', 'non', boolean]
    if form.validate_on_submit():
        mail = request.form.get('mail')
        MDP = request.form.get('MDP')
        print(mail)
        sql = f"SELECT email FROM Compte WHERE email = '{mail}'"
        db_instance = DBSingleton.Instance()
        temp = db_instance.query(sql)
        if len(temp) == 0:
            print('vide')
            print(temp)
        else:
            true_mail = temp[0][0]
            if true_mail == mail:
                print('bon mail')

                sql = f"SELECT mdp FROM Compte WHERE email = '{mail}'"
                print(sql)

                db_instance = DBSingleton.Instance()
                temp = db_instance.query(sql)
                print(temp)
                password = temp[0][0]

                print(MDP)
                """mot de passe prit part le insert"""
                print(f"le vrai mdp est {password}")
                if password == MDP:
                    print("bon mdp")
                    sql = f"SELECT role FROM Compte WHERE email = '{mail}' AND mdp = '{MDP}'"
                    print (sql)
                    db_instance = DBSingleton.Instance()
                    temp = db_instance.query(sql)
                    print(temp)
                    role = temp[0][0]
                    boolean = 1
                    retourner = [role, mail, MDP, boolean]
                else:
                    print("pas bon mdp")
    return retourner

def log():
    session = testlog()
    form = authform()
    role = session[0]
    boolean = session[3]
    print(f"auth bool is {boolean}")
    title = 'login'
    result = render_template('userconnect.html', form=form, title=title)
    if role == 1:
        result = redirect('/admin')
    elif role == 0:
        result = redirect('/user')
    return result

if __name__ == '__main__':
    app.run(debug=True)