import mysql.connector

class Singleton:
    def __init__(self, cls):
        self._cls = cls
    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance
    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')
    def __instancecheck__(self, instance):
        return isinstance(instance,self._cls)

@Singleton
class DBSingleton:
    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='root', host='localhost', database='HappyFly')
        pass
    def query(self, sql, params: tuple = ()):
        cursor = self.conn.cursor()
        cursor.execute(sql, params)
        result = cursor.fetchall()
        self.conn.commit()
        cursor.close
        return result
    def __str__(self):
        return 'Data connection object'
"""
class DBSingleton:
    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='root', host='localhost', database='HappyFly')
        pass

    def query(self, sql, params: tuple = ()):
        cursor = self.conn.cursor()
        cursor.execute(sql, params)
        try:
            self.result = cursor.fetchall()
        except mysql.connector.errors.InterfaceError:
            print('rien a reccup')
            self.result = False
            return self.result
        finally:
            self.conn.commit()
            cursor.close()
            return self.result

    def __str__(self):
        return 'Data connection object'
"""