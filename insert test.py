from connectDB import DBSingleton
import sys
id = 10
nom = 'bems'
prenom = 'will'
mdp = 'wil123'
mail = "willl@gmail.com"
buffday = '2002-02-14'
role = 1
try:
    record = (id, nom, prenom, mdp, mail, buffday, role)
    sql = "INSERT INTO Compte (CompteID, nom, prenom, mdp, email, DateDeNaissance, role) VALUES (%d,'%s','%s','%s','%s','%s',%d);" % record
    db_instance = DBSingleton.Instance()
    result = db_instance.query(sql)
    print('good')
except:
    print(sys.exc_info())
    print('pas bon')