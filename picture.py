# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'picture.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets  import *
from     PyQt5.QtCore   import    Qt
import numpy as np

class Ui_picture(object):
    def setupUi(self, Form,b):
        Form.setObjectName("Form")
        Form.resize(1029, 777)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -30, 1111, 841))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap('./data/orig/'+str(b)))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

