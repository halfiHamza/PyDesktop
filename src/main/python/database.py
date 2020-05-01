from mysql import connector
from datetime import datetime
from hashlib import md5


class MySQL(object):
    def __init__(self, server, user, password, database=None):
        self._server = server
        self._user = user
        self._password = password
        self._database = database

    def CreateDatabase(self):
        socket = connector.connect(user=self._user,
                                   password=self._password,
                                   host=self._server)
        cursor = socket.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(self._database))
        socket.commit()
        cursor.close()

    def execute_query(self, query, *args):
        try:
            socket = connector.connect(user = self._user,
                                       password = self._password,
                                       host = self._server,
                                       database = self._database)
            cursor = socket.cursor()
            cursor.execute(query, *args)
            result = cursor.fetchall()

            return socket, result
        except IOError:
            return False

    def CreateTables(self):
        try:
            self.execute_query('''
            CREATE TABLE `customers` (
              `id` int NOT NULL AUTO_INCREMENT,
              `full_name` varchar(50) NOT NULL,
              `device` varchar(50) NOT NULL,
              `mark` varchar(50) NOT NULL,
              `model` varchar(50) NOT NULL,
              `serial_num` varchar(50) NOT NULL,
              `date` datetime NOT NULL,
              `time` time NOT NULL,
              PRIMARY KEY (`id`))
            ''')
            self.execute_query('''
            CREATE TABLE `users` (
              `username` varchar(50) NOT NULL,
              `password` varchar(255) NOT NULL,
              `permission` varchar(5) NOT NULL)            
            ''')
            query = ("INSERT INTO users(username, password, permission) VALUES(%s, %s, %s)")
            self.execute_query(query, ["admin", md5('admin'.encode()).hexdigest(), "admin"])
            self.execute_query()[0].close()
            return True
        except:
            return False


    def Insert_data(self, data):
        history = datetime.now()
        date = history.strftime("%Y-%m-%d")
        time = history.strftime("%H:%M")
        data.append(date)
        data.append(time)
        query = "INSERT INTO customers (full_name, laptop, model, problem, date, time)" \
                " VALUES (%s, %s, %s, %s, %s, %s)"
        self.execute_query(query, data)

    def user_login(self, user_name, pwd):
        query = "SELECT permission FROM users WHERE username = %s AND password = MD5(%s)"
        result = self.execute_query(query,(user_name, pwd))
        result[0].close()

        return result


    @staticmethod
    def users(username, password, permission):
        pass
