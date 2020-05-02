from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QWidget
from RootUi import Ui_MainWindow
import LoginUi
import Config_db
import sys
import configparser
from database import MySQL



class MainCore:
    def __init__(self):
        self.appctxt = ApplicationContext()

    def resource(self, source_name):
        return self.appctxt.get_resource(source_name)

    def exit(self):
         exit_code = self.appctxt.app.exec_()
         return sys.exit(exit_code)

class ConfigParser:
    pass


class Login(QWidget, MainCore, LoginUi.Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Login Form')
        self.exit_btn.clicked.connect(self.close)
        self.login_btn.clicked.connect(self.Authentication)

    def Authentication(self):
        path = MainCore()
        file = configparser.ConfigParser()
        file.read(path.resource('config.ini'))
        operation = MySQL(file.get('DATABASE', 'host'),
                          file.get('DATABASE', 'user'),
                          file.get('DATABASE', 'password'),
                          file.get('DATABASE', 'database'))
        result = operation.user_login(self.user_name.text(), self.password.text())
        if  len(list(result[1])) == 0:
            self.label_error.setStyleSheet('color: red')
            self.label_error.setText('Access denied !')
        else:
            permission = result[1][0]
            RootWindow.show()
            self.close()


class Config(QWidget, Config_db.Ui_Form, MainCore):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Config Form')
        self.file = configparser.ConfigParser()
        self.path = MainCore()
        self.file.read(self.path.resource('config.ini'))
        self.serverHost.setText(self.file.get('DATABASE', 'host'))
        self.userName.setText(self.file.get('DATABASE', 'user'))
        self.password.setText(self.file.get('DATABASE', 'password'))
        self.databaseName.setText(self.file.get('DATABASE', 'database'))

        self.save_btn.clicked.connect(self.setChange)
        self.dbCheck_btn.clicked.connect(self.create_db)
        self.Exit_btn.clicked.connect(self.close)

    @property
    def get_config(self):
        host = self.serverHost.text()
        user = self.userName.text()
        pwd = self.password.text()
        db_name = self.databaseName.text().lower()

        return host, user, pwd, db_name

    def setChange(self):
        self.file['DATABASE']['host'] = self.serverHost.text()
        self.file['DATABASE']['user'] = self.userName.text()
        self.file['DATABASE']['password'] = self.password.text()
        self.file['DATABASE']['database'] = self.databaseName.text().lower()
        with open(self.path.resource('config.ini'), 'w') as config:
            self.file.write(config)
        self.save_label.setStyleSheet('color: green')
        self.save_label.setText('Saved to Config')

    def create_db(self):
        def field():
            for i in list(self.get_config):
                if i == '':
                    self.status_label.setStyleSheet("color: red;")
                    self.status_label.setText('Empty field !')
                    return False
                else:
                    return True
        if field():
            db = MySQL(self.get_config[0], self.get_config[1], self.get_config[2], self.get_config[3])
            db.CreateDatabase()
            if db.CreateTables():
                self.status_label.setStyleSheet("color: green;")
                self.status_label.setText('Success Connect')
                self.save_btn.setEnabled(True)
            else:
                self.status_label.setStyleSheet("color: red;")
                self.status_label.setText("Access denied!")



class RootWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('WORKSHOP Management')
        #self.setWindowFlag(Qt.FramelessWindowHint)


if __name__ == '__main__':
    app = MainCore()

    config = configparser.ConfigParser()
    config.read(app.resource('config.ini'))
    database = config['DATABASE']['database']
    if database == '':
        configWindow = Config()
        configWindow.show()
    else:
        loginWindow = Login()
        loginWindow.show()

    app.exit()
