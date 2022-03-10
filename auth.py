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

if __name__ == '__main__':
    def genformlog():
        form = authform()
        return render_template('titanic.html', form=form)


    @app.route('/titanic/adduser')
    def temp():
        return ("hello")

    @app.route('/titanic/admin', methods=['POST', 'GET'])
    def login():
        form = authform()
        if form.validate_on_submit():
            mail = request.form.get('mail')
            MDP = request.form.get('MDP')
            print(mail)
            sql = f"SELECT email FROM Compte WHERE role = 1 AND email = '{mail}'"
            db_instance = DBSingleton.Instance()
            temp = db_instance.query(sql)
            if len(temp) == 0:
                print('vide')
                print(temp)
            else:
                true_mail = temp[0][0]
                if true_mail == mail:
                    print('bon mail')

                    sql = f"SELECT mdp FROM Compte WHERE role = 1 AND email = '{mail}'"
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
                        retouner = redirect('/titanic/adduser')
                    else:
                        print("pas bon mdp")
        return retouner
if __name__ == '__main__':
    app.run(debug=True)