from connectDB import DBSingleton

mail = "jesuisunadmin@gmail.com"
MDP = "root"
sql = f"SELECT compteID FROM Compte WHERE email = '{mail}' AND mdp = '{MDP}'"
db_instance = DBSingleton.Instance()
posts = db_instance.query(sql)
if len(posts) == 0:
    print('pas bon')
else:
    print('bon')
    result = str(posts[0])[2:-3]
    print(result)
    if mail == result:
        print('good')
    else:
        print('pas bon')