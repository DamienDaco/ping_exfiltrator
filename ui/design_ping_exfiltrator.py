# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_ping_exfiltrator.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(287, 293)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setObjectName("stop_button")
        self.gridLayout.addWidget(self.stop_button, 4, 1, 1, 1)
        self.ip_label = QtWidgets.QLabel(self.centralwidget)
        self.ip_label.setObjectName("ip_label")
        self.gridLayout.addWidget(self.ip_label, 2, 0, 1, 2)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.gridLayout.addWidget(self.start_button, 4, 0, 1, 1)
        self.text_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_browser.setObjectName("text_browser")
        self.gridLayout.addWidget(self.text_browser, 1, 0, 1, 2)
        self.ip_line = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_line.setClearButtonEnabled(True)
        self.ip_line.setObjectName("ip_line")
        self.gridLayout.addWidget(self.ip_line, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.sender_button = QtWidgets.QRadioButton(self.centralwidget)
        self.sender_button.setObjectName("sender_button")
        self.gridLayout.addWidget(self.sender_button, 0, 0, 1, 1)
        self.receiver_button = QtWidgets.QRadioButton(self.centralwidget)
        self.receiver_button.setObjectName("receiver_button")
        self.gridLayout.addWidget(self.receiver_button, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 287, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.menuFile.addAction(self.action_open)
        self.menubar.addAction(self.menuFile.menuAction())
        self.ip_label.setBuddy(self.ip_line)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ping Exfiltrator"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.ip_label.setText(_translate("MainWindow", "IP address:"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.ip_line.setPlaceholderText(_translate("MainWindow", "x.x.x.x"))
        self.sender_button.setText(_translate("MainWindow", "Sender"))
        self.receiver_button.setText(_translate("MainWindow", "Receiver"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_open.setText(_translate("MainWindow", "Open"))

