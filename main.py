from connectDB import DBSingleton
sql = 'select * from Compte'
db_instance = DBSingleton.Instance()
result = db_instance.query(sql)
print(result)