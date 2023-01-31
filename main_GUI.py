
# from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog, QApplication, QWidget
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
import numpy as np
import pandas as pd
import picture
import res_pic
from glob import glob
import os
import main as Lanet
import cv2
from sklearn.metrics import cohen_kappa_score

a=[]

class Ui_widget(object):
    def __init__(self):
        self.columnNum = 19
        self.RowNum = 100
        self._addPhy = 0
        self._addPhyFlag = False
        self.Phylabel = []
        self.PhyNameBox = []
        self.PhyOpinBox = []
        self.fname = []
        self.outputImage = []
        self._translate = QtCore.QCoreApplication.translate
        self.all_class_list = [] # list of observed class for all images that used in Fleiss Kappa
        self.all_phy_opin = []
        self.alg_res_list = []
        self.alg_prob_list = []
        self.notFirstRow = False


    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(1024, 605)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        widget.setPalette(palette)
        self.line = QtWidgets.QFrame(widget)
        self.line.setGeometry(QtCore.QRect(10, 190, 1004, 51))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.groupBox = QtWidgets.QGroupBox(widget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 241, 190))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 255, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 255, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 255, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.groupBox.setPalette(palette)
        self.groupBox.setObjectName("groupBox")
        # Age field
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 61, 25))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self._AgeBox = QtWidgets.QLineEdit(self.groupBox)
        self._AgeBox.setGeometry(QtCore.QRect(90, 30, 113, 25))
        self._AgeBox.setObjectName("lineEdit")
        # File Name Group
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 71, 25))
        self.label_5.setObjectName("label_5")
        self._FileNameBox = QtWidgets.QLineEdit(self.groupBox)
        self._FileNameBox.setGeometry(QtCore.QRect(90, 70, 113, 25))
        self._FileNameBox.setObjectName("_FileNameBox")
        self.pushButton_3 = QtWidgets.QPushButton(widget)
        self.pushButton_3.setGeometry(QtCore.QRect(225, 80, 31, 25))
        self.pushButton_3.setObjectName("pushButton_3")

        # Doctor 1 Group
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 71, 25))
        self.label_2.setObjectName("label_2")
        self.F_PhyNameBox = QtWidgets.QLineEdit(self.groupBox)
        self.F_PhyNameBox.setGeometry(QtCore.QRect(90, 110, 113, 25))
        self.F_PhyNameBox.setObjectName("F_PhyNameBox")

        self.F_PhyOpinBox = QtWidgets.QLineEdit(self.groupBox)
        self.F_PhyOpinBox.setGeometry(QtCore.QRect(205, 110, 31, 25))
        self.F_PhyOpinBox.setObjectName("F_PhyOpinBox")

        # Physician Add Button
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 71, 25))
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(widget)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 160, 147, 25))  #push button axis: x+20 and y+10 with respect the other label in column
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.addPhysician)

        # Table design
        self.tableWidget = QtWidgets.QTableWidget(widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setGeometry(QtCore.QRect(20, 230, 980, 351))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)

        self.tableWidget.setColumnCount(self.columnNum)
        self.tableWidget.setRowCount(self.RowNum)
        for i in range(self.RowNum):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

        for i in range(self.columnNum):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)

        for i in range(0,self.RowNum):
            self.tableWidget.setItem(i, 5, item)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)

            self.tableWidget.setItem(i, 6, item)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)

        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(9, 7, item)
        self.pushButton = QtWidgets.QPushButton(widget)
        self.pushButton.setGeometry(QtCore.QRect(600, 100, 171, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(widget)
        self.pushButton_2.setGeometry(QtCore.QRect(820, 60, 171, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(widget)
        self.pushButton_5.setGeometry(QtCore.QRect(820, 140, 171, 31))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        # self._translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(self._translate("widget", "Metaplasia Detector"))
        self.groupBox.setTitle(self._translate("widget", " Information"))
        self.label.setText(self._translate("widget", "Age:"))
        self.label_2.setText(self._translate("widget", "Physician:"))
        self.label_3.setText(self._translate("widget", "Physician:"))
        self.label_5.setText(self._translate("widget", "DIR Name: "))
        for i in range(self.RowNum):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(self._translate("widget", str(i+1)))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(self._translate("widget", "File Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(self._translate("widget", "Age"))
        # item.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(self._translate("widget", "ALG. Result"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(self._translate("widget", "ALG. Probability %"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(self._translate("widget", "Cohen's Kappa"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(self._translate("widget", "Ori_Image"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(self._translate("widget", "Res_Image"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(self._translate("widget", "Phy. Name"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(self._translate("widget", "Phy. Opinion"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        header = self.tableWidget.horizontalHeader()
        [header.setSectionResizeMode(i, QHeaderView.ResizeToContents) for i in range(self.columnNum)]

        for i in range(0,self.RowNum):
            item = self.tableWidget.item(i, 5)
            item.setText(self._translate("widget", "Orig_Image"))
            item = self.tableWidget.item(i, 6)
            item.setText(self._translate("widget", "Res_Image"))


        self.pushButton.setText(self._translate("widget", "RUN"))
        self.pushButton_2.setText(self._translate("widget", "Export File"))
        self.pushButton_3.setText(self._translate("widget","..."))
        self.pushButton_4.setText(self._translate("widget", "+"))
        self.pushButton_5.setText(self._translate("widget", "Upload File"))

        self.pushButton.clicked.connect(lambda :  self.ImAlgorithm())
        self.tableWidget.doubleClicked.connect(lambda :  self.delet_show())
        self.tableWidget.itemChanged.connect(self.on_itemChanged)
        self.pushButton_2.clicked.connect(lambda : self.exportToExcel())
        self.pushButton_3.clicked.connect(lambda :self.browsefile())
        self.pushButton_5.clicked.connect(lambda : self._upload_file())

    # add physician routine
    def addPhysician(self):
        try:
            if self._addPhy < 5:
                self._addPhyFlag = True
                # self._translate = QtCore.QCoreApplication.translate
                palette = QtGui.QPalette()
                if self._addPhy == 0:
                    self.groupBox_2 = QtWidgets.QGroupBox(widget)
                    self.groupBox_2.setGeometry(QtCore.QRect(270, 10, 241, 190))
                    self.groupBox_2.setPalette(palette)
                    self.groupBox_2.setObjectName("groupBox_2")
                    self.groupBox_2.setTitle(self._translate("widget", " Physician Opinion"))

                self.Phylabel.append(QtWidgets.QLabel(self.groupBox_2))
                self.Phylabel[self._addPhy].setGeometry(QtCore.QRect(10, 30+self._addPhy*30, 71, 25))
                self.Phylabel[self._addPhy].setObjectName("Phylabel"+str(self._addPhy))

                self.PhyNameBox.append(QtWidgets.QLineEdit(self.groupBox_2))
                self.PhyNameBox[self._addPhy].setGeometry(QtCore.QRect(90, 30+self._addPhy*30, 113, 25))
                self.PhyNameBox[self._addPhy].setObjectName("PhyNameBox"+str(self._addPhy))
                self.PhyOpinBox.append(QtWidgets.QLineEdit(self.groupBox_2))
                self.PhyOpinBox[self._addPhy].setGeometry(QtCore.QRect(205, 30+self._addPhy*30, 31, 25))
                self.PhyOpinBox[self._addPhy].setObjectName("PhyOpinBox"+str(self._addPhy))
                self.Phylabel[self._addPhy].setText(self._translate("widget", "Physician:"))
                self.groupBox_2.show()
                self.Phylabel[self._addPhy].show()
                self.PhyNameBox[self._addPhy].show()
                self.PhyOpinBox[self._addPhy].show()
                self._addPhy = self._addPhy+1
            else:
                self.popup("The number of Physician is out of range")
        except:
            self.popup('Please Check the Physician`s opinons')
    def browsefile(self):
        try:
            self._dir_ = QFileDialog.getExistingDirectory()
            self._FileNameBox.setText(self._dir_.split('/')[-1])
        except:
            self.popup('Please select Correct Folder')
    def delet_show(self):
        for idx in self.tableWidget.selectionModel().selectedIndexes():
            if(idx.column()==5):
                p=picture.Ui_picture()
                q=QtWidgets.QDialog()
                p.setupUi(q,self.fname[idx.row()])
                q.exec_()

            if (idx.column() == 6):
                p = res_pic.Ui_picture()
                q = QtWidgets.QDialog()
                p.setupUi(q, self.outputImage[idx.row()])
                q.exec_()
# -------------------------------------------------------------------------------------------
#   Function of Run Button
# -------------------------------------------------------------------------------------------
    def ImAlgorithm(self):
        # popup if the value of Physician opinion is out of range
        if self.F_PhyOpinBox.text() != '':
            if int(self.F_PhyOpinBox.text()) != 0 and int(self.F_PhyOpinBox.text()) != 1:
                self.popup()
                return None
        if self._addPhyFlag:
            for i in range(self._addPhy):
                if self.PhyOpinBox[i].text() != '':
                    if int(self.PhyOpinBox[i].text()) != 0 and int(self.PhyOpinBox[i].text()) != 1:
                        self.popup()
                        return None
        try:
            alg = Lanet.main(self._dir_)
            classes_pred, probs = alg.run()
            self.alg_res=[]
            for class_pred in classes_pred:
                self.alg_res.append(int(class_pred))  # class prediction
            for prob in probs:
                self.alg_prob_list.append(int(prob))  # Probability of prediction
            for i in list(range(0,self.RowNum)):
                self.tab=self.tableWidget.item(i,0)
                if   self.tab==None :
                    self.ROW=i
                    break

            setPaths = []
            for data_path in glob(self._dir_ + "/Results/original" + "/*"):
                self.fname.append(data_path)
                self.outputImage.append(self._dir_ + '/Results/shape/'+data_path.split('\\')[-1])

            # import data in table
            for i in range(len(self.alg_res)):
                self.tableWidget.setItem(self.ROW+i, 1,QTableWidgetItem(self._AgeBox.text()))
                self.tableWidget.setItem(self.ROW+i, 0,QTableWidgetItem(self.fname[i+self.ROW].split('\\')[-1]))
                self.tableWidget.setItem(self.ROW+i, 2,QTableWidgetItem(str(self.alg_res[i])))
                self.tableWidget.setItem(self.ROW+i, 3,QTableWidgetItem((str(self.alg_prob_list[i]))))

                self.tableWidget.setItem(self.ROW+i, 7,QTableWidgetItem(self.F_PhyNameBox.text()))
                self.tableWidget.setItem(self.ROW+i, 8, QTableWidgetItem(self.F_PhyOpinBox.text()))
            if self._addPhyFlag:
                for i in range(self._addPhy):
                    if i<5:
                        item = self.tableWidget.horizontalHeaderItem(9 + 2 * i)
                        item.setText(self._translate("widget", 'Phy. Name' ))
                        item = self.tableWidget.horizontalHeaderItem(10 + 2 * i)
                        item.setText(self._translate("widget", 'Phy. Opinion'))
                        for j in range(len(self.alg_res)):
                            self.tableWidget.setItem(self.ROW+j,
                                                     9 + 2 * i,
                                                     QTableWidgetItem(self.PhyNameBox[i].text()))

                            self.tableWidget.setItem(self.ROW+j,
                                                     10 + 2 * i,
                                                     QTableWidgetItem(self.PhyOpinBox[i].text()))
            for item in self.alg_res:
                self.alg_res_list.append(item)
            self._cohenskappa()
        except:
            self.popup('Please check the Directory name')

    def on_itemChanged(self):
        for idx in self.tableWidget.selectionModel().selectedIndexes():
            if idx.column() in [8,10,12,14,16,18]:
                self._cohenskappa()

    def _cohenskappa(self):

        self.alg_con =[]
        phyopin_row = []
        for _row in range(self.tableWidget.rowCount()):
            phyopin_col=[]
            if self.tableWidget.item(_row, 3) != None: # Check for having data in the row
                for col in [8,10,12,14,16,18]: # column number of phy. opinion
                    if self.tableWidget.item(_row,col)  != None:
                        if self.tableWidget.item(_row,col).text() != '':
                            phyopin_col.append(int(float(self.tableWidget.item(_row, col).text())))
                if len(phyopin_col) != 0:
                    # self.alg_res_list.append(int(self.alg_res))
                    n, _maxopin = max((phyopin_col.count(_idx), _idx) for _idx in set(phyopin_col))
                    phyopin_row.append(_maxopin)
                try:
                    if self.alg_res_list[:_row+1] != phyopin_row:
                        self.alg_con.append(str(np.round(cohen_kappa_score(self.alg_res_list[:_row+1], phyopin_row),3)))
                    else:
                        self.alg_con.append('Same Result')
                except:
                    self.alg_con.append('-')
                self.tableWidget.blockSignals(True)
                self.tableWidget.setItem(_row,4,QTableWidgetItem(str(self.alg_con[_row])))
                self.tableWidget.blockSignals(False)
    def popup(self, txt="Please Check the Parameters"):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText(txt)
        x = msg.exec_()

    def get_column_data(self, column):
        data = []
        for i in range(self.tableWidget.rowCount()):
            data.append(self.tableWidget.item(i, column).text())
        return data
    def _upload_file(self):
        try:
            _Upload_csv_Name, ok = QFileDialog.getOpenFileName(filter='*.csv',
                                                      caption="Import endoscopic Image",
                                                      directory="./")
            for i in range(self.RowNum):
                if self.tableWidget.item(i, 0) == None:
                    extendRow = i
                    break
            df = pd.read_csv(_Upload_csv_Name)
            for row in range(df.shape[0]):
                for col in range(df.shape[1]):
                    if not pd.isnull(df.iloc[row, col]):
                        if col == 5:
                            self.fname.append(df.iloc[row , col])
                        elif col == 6:
                            self.outputImage.append((df.iloc[row, col]))
                        else:
                            self.tableWidget.setItem(row + extendRow, col, QTableWidgetItem(str(df.iloc[row, col])))
                            if col == 2:
                                self.alg_res_list.append(float(df.iloc[row, col]))
                            elif col ==3:
                                self.alg_prob_list.append(float(df.iloc[row, col]))
        except:
            self.popup('Please Select Correct File')

    def exportToExcel(self):
        # take path and name file for save the data
        try:
            path, ok = QtWidgets.QFileDialog.getSaveFileName(parent=None,directory='./',filter='*.csv')


            df = pd.DataFrame()

            # create dataframe object recordset
            for row in range(0, self.tableWidget.rowCount()):
                for col in range(0, self.tableWidget.columnCount()):
                    if self.tableWidget.item(row, col) != None:
                        if col == 5:
                            if self.tableWidget.item(row, 0) != None:
                                df.at[row, col] = self.fname[row]
                            else:
                                df.at[row, col] = ''
                        elif col == 6:
                            if self.tableWidget.item(row, 0) != None:
                                df.at[row, col] = self.outputImage[row]
                            else:
                                df.at[row, col] = ''
                        else:
                            df.at[row, col] = self.tableWidget.item(row, col).text()

            # create column header list
            columnHeaders = []
            for j in range(self.tableWidget.model().columnCount()):
                if self.tableWidget.horizontalHeaderItem(j).text() != '':
                    columnHeaders.append(self.tableWidget.horizontalHeaderItem(j).text())
            df.set_axis(columnHeaders,axis=1,inplace=True)
            df.to_csv(path+'.csv', index=False)
            self.popup(txt='Excel file was exported')
        except:
            self.popup('Please Check the exported data')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_widget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())

