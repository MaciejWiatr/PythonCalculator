# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 471)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(471, 471))
        MainWindow.setMaximumSize(QtCore.QSize(471, 471))
        MainWindow.setStyleSheet("background-color: rgb(60, 60, 60);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 452))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 180, 331, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.threeButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.threeButton.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.threeButton.setFont(font)
        self.threeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.threeButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(40, 40, 40);\n"
"border: none;\n"
"padding: 10px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"height: 75%;\n"
"width: 75%;\n"
"}\n"
"")
        self.threeButton.setObjectName("threeButton")
        self.gridLayout.addWidget(self.threeButton, 0, 2, 1, 1)
        self.fourButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.fourButton.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.fourButton.setFont(font)
        self.fourButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fourButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(40, 40, 40);\n"
"border: none;\n"
"padding: 10px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"height: 75%;\n"
"width: 75%;\n"
"}\n"
"")
        self.fourButton.setObjectName("fourButton")
        self.gridLayout.addWidget(self.fourButton, 1, 0, 1, 1)
        self.nineButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.nineButton.setMinimumSize(QtCore.QSize(0, 80))
        self.nineButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.nineButton.setFont(font)
        self.nineButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nineButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(40, 40, 40);\n"
"border: none;\n"
"padding: 10px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"height: 75%;\n"
"width: 75%;\n"
"}\n"
"")
        self.nineButton.setObjectName("nineButton")
        self.gridLayout.addWidget(self.nineButton, 2, 2, 1, 1)
        self.oneButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oneButton.sizePolicy().hasHeightForWidth())
        self.oneButton.setSizePolicy(sizePolicy)
        self.oneButton.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.oneButton.setFont(font)
        self.oneButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.oneButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(40, 40, 40);\n"
"border: none;\n"
"padding: 10px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"height: 75%;\n"
"width: 75%;\n"
"}\n"
"\n"
"\n"
"")
        self.oneButton.setObjectName("oneButton")
        self.gridLayout.addWidget(self.oneButton, 0, 0, 1, 1)
        self.twoButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.twoButton.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.twoButton.setFont(font)
        self.twoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.twoButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(40, 40, 40);\n"
"border: none;\n"
"padding: 10px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"height: 75%;\n"
"width: 75%;\n"
"}\n"
"")
        self.twoButton.setObjectName("twoButton")
        self.gridLayout.addWidget(self.twoButton, 0, 1, 1, 1)
        self.sixButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sixButton.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.sixButton.setFont(font)
        self.sixButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sixButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(40, 40, 40);\n"
"border: none;\n"
"padding: 10px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"height: 75%;\n"
"width: 75%;\n"
"}\n"
"")
        self.sixButton.setObjectName("sixButton")
        self.gridLayout.addWidget(self.sixButton, 1, 2, 1, 1)
        self.sevenButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sevenButton.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.sevenButton.setFont(font)
        self.sevenButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sevenButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(40, 40, 40);\n"
"border: none;\n"
"padding: 10px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"height: 75%;\n"
"width: 75%;\n"
"}\n"
"\n"
"\n"
"")
        self.sevenButton.setObjectName("sevenButton")
        self.gridLayout.addWidget(self.sevenButton, 2, 0, 1, 1)
        self.eightButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.eightButton.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.eightButton.setFont(font)
        self.eightButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eightButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(40, 40, 40);\n"
"border: none;\n"
"padding: 10px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"height: 75%;\n"
"width: 75%;\n"
"}\n"
"\n"
"")
        self.eightButton.setObjectName("eightButton")
        self.gridLayout.addWidget(self.eightButton, 2, 1, 1, 1)
        self.fiveButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.fiveButton.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.fiveButton.setFont(font)
        self.fiveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fiveButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(40, 40, 40);\n"
"border: none;\n"
"padding: 10px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"height: 75%;\n"
"width: 75%;\n"
"}\n"
"")
        self.fiveButton.setObjectName("fiveButton")
        self.gridLayout.addWidget(self.fiveButton, 1, 1, 1, 1)
        self.resultBox = QtWidgets.QLineEdit(self.centralwidget)
        self.resultBox.setGeometry(QtCore.QRect(10, 10, 451, 101))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.resultBox.setFont(font)
        self.resultBox.setStyleSheet("color: white;\n"
"background-color: rgb(40,40,40);\n"
"border: None;\n"
"padding: 5px;\n"
"")
        self.resultBox.setText("")
        self.resultBox.setObjectName("resultBox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 120, 331, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.clearButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMinimumSize(QtCore.QSize(0, 50))
        self.clearButton.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.clearButton.setFont(font)
        self.clearButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(173, 41, 41);\n"
"color: white;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(183, 51, 51);\n"
"color: white;\n"
"border: none;\n"
"}")
        self.clearButton.setIconSize(QtCore.QSize(40, 40))
        self.clearButton.setObjectName("clearButton")
        self.gridLayout_2.addWidget(self.clearButton, 0, 2, 1, 1)
        self.sumButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sumButton.sizePolicy().hasHeightForWidth())
        self.sumButton.setSizePolicy(sizePolicy)
        self.sumButton.setMinimumSize(QtCore.QSize(0, 50))
        self.sumButton.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.sumButton.setFont(font)
        self.sumButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sumButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(173, 41, 41);\n"
"color: white;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(183, 51, 51);\n"
"color: white;\n"
"border: none;\n"
"}")
        self.sumButton.setIconSize(QtCore.QSize(40, 40))
        self.sumButton.setObjectName("sumButton")
        self.gridLayout_2.addWidget(self.sumButton, 0, 0, 1, 1)
        self.zeroButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zeroButton.sizePolicy().hasHeightForWidth())
        self.zeroButton.setSizePolicy(sizePolicy)
        self.zeroButton.setMinimumSize(QtCore.QSize(0, 50))
        self.zeroButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.zeroButton.setFont(font)
        self.zeroButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zeroButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(40, 40, 40);\n"
"border: none;\n"
"padding: 10px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"height: 75%;\n"
"width: 75%;\n"
"}\n"
"\n"
"")
        self.zeroButton.setObjectName("zeroButton")
        self.gridLayout_2.addWidget(self.zeroButton, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(350, 180, 111, 261))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.divideButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.divideButton.setMinimumSize(QtCore.QSize(0, 80))
        self.divideButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.divideButton.setFont(font)
        self.divideButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.divideButton.setStyleSheet("\n"
"QPushButton{\n"
"background-color:rgb(86, 86, 86);\n"
"color: white;\n"
"border: none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(96, 96, 96);\n"
"color: white;\n"
"border: none;\n"
"\n"
"}")
        self.divideButton.setObjectName("divideButton")
        self.gridLayout_3.addWidget(self.divideButton, 3, 0, 1, 1)
        self.timesButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.timesButton.setMinimumSize(QtCore.QSize(0, 80))
        self.timesButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.timesButton.setFont(font)
        self.timesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.timesButton.setStyleSheet("\n"
"QPushButton{\n"
"background-color:rgb(86, 86, 86);\n"
"color: white;\n"
"border: none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(96, 96, 96);\n"
"color: white;\n"
"border: none;\n"
"\n"
"}")
        self.timesButton.setObjectName("timesButton")
        self.gridLayout_3.addWidget(self.timesButton, 2, 0, 1, 1)
        self.minusButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.minusButton.setMinimumSize(QtCore.QSize(0, 80))
        self.minusButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.minusButton.setFont(font)
        self.minusButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minusButton.setStyleSheet("\n"
"QPushButton{\n"
"background-color:rgb(86, 86, 86);\n"
"color: white;\n"
"border: none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(96, 96, 96);\n"
"color: white;\n"
"border: none;\n"
"\n"
"}")
        self.minusButton.setObjectName("minusButton")
        self.gridLayout_3.addWidget(self.minusButton, 1, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(350, 120, 111, 61))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plusButton = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plusButton.sizePolicy().hasHeightForWidth())
        self.plusButton.setSizePolicy(sizePolicy)
        self.plusButton.setMinimumSize(QtCore.QSize(0, 50))
        self.plusButton.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.plusButton.setFont(font)
        self.plusButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plusButton.setStyleSheet("\n"
"QPushButton{\n"
"background-color:rgb(86, 86, 86);\n"
"color: white;\n"
"border: none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(96, 96, 96);\n"
"color: white;\n"
"border: none;\n"
"\n"
"}")
        self.plusButton.setIconSize(QtCore.QSize(40, 40))
        self.plusButton.setObjectName("plusButton")
        self.gridLayout_4.addWidget(self.plusButton, 0, 0, 1, 1)
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(390, 10, 71, 20))
        self.errorLabel.setStyleSheet("background-color: rgb(40,40,40);\n"
"color: red;\n"
"text-align: center;")
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PythonCalculator"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.resultBox.setPlaceholderText(_translate("MainWindow", "Your result"))
        self.clearButton.setText(_translate("MainWindow", "CE"))
        self.sumButton.setText(_translate("MainWindow", "="))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.timesButton.setText(_translate("MainWindow", "x"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.errorLabel.setText(_translate("MainWindow", "TextLabel"))

