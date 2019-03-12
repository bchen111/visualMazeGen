# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MazeMainWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 610)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_selectGenerateMethod = QtWidgets.QWidget(self.centralwidget)
        self.widget_selectGenerateMethod.setObjectName("widget_selectGenerateMethod")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_selectGenerateMethod)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_selectGenerateMethod = QtWidgets.QComboBox(self.widget_selectGenerateMethod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_selectGenerateMethod.sizePolicy().hasHeightForWidth())
        self.comboBox_selectGenerateMethod.setSizePolicy(sizePolicy)
        self.comboBox_selectGenerateMethod.setObjectName("comboBox_selectGenerateMethod")
        self.comboBox_selectGenerateMethod.addItem("")
        self.comboBox_selectGenerateMethod.addItem("")
        self.comboBox_selectGenerateMethod.addItem("")
        self.comboBox_selectGenerateMethod.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_selectGenerateMethod)
        self.label_mazeSize = QtWidgets.QLabel(self.widget_selectGenerateMethod)
        self.label_mazeSize.setObjectName("label_mazeSize")
        self.horizontalLayout.addWidget(self.label_mazeSize)
        self.spinBox_mazeSize = QtWidgets.QSpinBox(self.widget_selectGenerateMethod)
        self.spinBox_mazeSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox_mazeSize.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_mazeSize.setMinimum(5)
        self.spinBox_mazeSize.setProperty("value", 20)
        self.spinBox_mazeSize.setObjectName("spinBox_mazeSize")
        self.horizontalLayout.addWidget(self.spinBox_mazeSize)
        self.pushButton_generatorRun = QtWidgets.QPushButton(self.widget_selectGenerateMethod)
        self.pushButton_generatorRun.setObjectName("pushButton_generatorRun")
        self.horizontalLayout.addWidget(self.pushButton_generatorRun)
        self.horizontalLayout.setStretch(0, 100)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addWidget(self.widget_selectGenerateMethod)
        self.widget_mazeDisplay = QtWidgets.QWidget(self.centralwidget)
        self.widget_mazeDisplay.setMinimumSize(QtCore.QSize(400, 400))
        self.widget_mazeDisplay.setObjectName("widget_mazeDisplay")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_mazeDisplay)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_mazeDisplayMain = MazeDisplay(self.widget_mazeDisplay)
        self.widget_mazeDisplayMain.setObjectName("widget_mazeDisplayMain")
        self.horizontalLayout_2.addWidget(self.widget_mazeDisplayMain)
        self.horizontalLayout_2.setStretch(0, 1)
        self.verticalLayout.addWidget(self.widget_mazeDisplay)
        self.widget_selectSolveMethod = QtWidgets.QHBoxLayout()
        self.widget_selectSolveMethod.setObjectName("widget_selectSolveMethod")
        self.comboBox_seleveSolveMethod = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_seleveSolveMethod.setObjectName("comboBox_seleveSolveMethod")
        self.comboBox_seleveSolveMethod.addItem("")
        self.comboBox_seleveSolveMethod.addItem("")
        self.comboBox_seleveSolveMethod.addItem("")
        self.comboBox_seleveSolveMethod.addItem("")
        self.widget_selectSolveMethod.addWidget(self.comboBox_seleveSolveMethod)
        self.pushButton_solverRun = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_solverRun.setObjectName("pushButton_solverRun")
        self.widget_selectSolveMethod.addWidget(self.pushButton_solverRun)
        self.widget_selectSolveMethod.setStretch(0, 100)
        self.widget_selectSolveMethod.setStretch(1, 1)
        self.verticalLayout.addLayout(self.widget_selectSolveMethod)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_generatorRun.clicked.connect(MainWindow.mainFunc_generatorRun)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Maze - bchen111"))
        self.comboBox_selectGenerateMethod.setItemText(0, _translate("MainWindow", "Generator - Recursive Backtracking"))
        self.comboBox_selectGenerateMethod.setItemText(1, _translate("MainWindow", "Kruskal\'s Algorithm"))
        self.comboBox_selectGenerateMethod.setItemText(2, _translate("MainWindow", "Prim\'s Algorithm"))
        self.comboBox_selectGenerateMethod.setItemText(3, _translate("MainWindow", "Hunt And Kill"))
        self.label_mazeSize.setText(_translate("MainWindow", "Maze size"))
        self.pushButton_generatorRun.setText(_translate("MainWindow", "Run"))
        self.comboBox_seleveSolveMethod.setItemText(0, _translate("MainWindow", "Solver - Depth First Search"))
        self.comboBox_seleveSolveMethod.setItemText(1, _translate("MainWindow", "Breadth First Search"))
        self.comboBox_seleveSolveMethod.setItemText(2, _translate("MainWindow", "Dijkstra Algorithm"))
        self.comboBox_seleveSolveMethod.setItemText(3, _translate("MainWindow", "A* Algorithm"))
        self.pushButton_solverRun.setText(_translate("MainWindow", "Run"))

from MazeDisplay import MazeDisplay
