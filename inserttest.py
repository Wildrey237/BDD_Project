from connectDB import DBSingleton
import sys

nom = 'bas'
prenom = 'bast'
mdp = 'rgred'
mail = "bastt@gmail.com"
buffday = '2002-02-14'
role = 0
try:
    record = (nom, prenom, mdp, mail, buffday, role)
    sql = "INSERT INTO Compte (nom, prenom, mdp, email, DateDeNaissance, role) VALUES ('%s','%s','%s','%s','%s',%d);" % record
    db_instance = DBSingleton.Instance()
    db_instance.query(sql)
    print('good')
except:
    print(sys.exc_info())
    print('pas bon')