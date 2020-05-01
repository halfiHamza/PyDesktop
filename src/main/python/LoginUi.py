# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 300)
        Form.setMinimumSize(QtCore.QSize(300, 300))
        Form.setMaximumSize(QtCore.QSize(300, 300))
        self.user_name = QtWidgets.QLineEdit(Form)
        self.user_name.setGeometry(QtCore.QRect(60, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_name.setFont(font)
        self.user_name.setMaxLength(30)
        self.user_name.setAlignment(QtCore.Qt.AlignCenter)
        self.user_name.setObjectName("user_name")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(60, 150, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setMaxLength(30)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 20, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.login_btn = QtWidgets.QPushButton(Form)
        self.login_btn.setGeometry(QtCore.QRect(60, 260, 75, 23))
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_btn.setObjectName("login_btn")
        self.exit_btn = QtWidgets.QPushButton(Form)
        self.exit_btn.setGeometry(QtCore.QRect(150, 260, 75, 23))
        self.exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_btn.setObjectName("exit_btn")
        self.label_error = QtWidgets.QLabel(Form)
        self.label_error.setGeometry(QtCore.QRect(60, 220, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_error.setFont(font)
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.pwd_checkBox = QtWidgets.QCheckBox(Form)
        self.pwd_checkBox.setGeometry(QtCore.QRect(60, 190, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pwd_checkBox.setFont(font)
        self.pwd_checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pwd_checkBox.setObjectName("pwd_checkBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.user_name.setPlaceholderText(_translate("Form", "user name"))
        self.password.setPlaceholderText(_translate("Form", "password"))
        self.label.setText(_translate("Form", "Login Form"))
        self.login_btn.setText(_translate("Form", "Login"))
        self.exit_btn.setText(_translate("Form", "Exit"))
        self.pwd_checkBox.setText(_translate("Form", "View password"))
