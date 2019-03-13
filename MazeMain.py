# -*- coding: utf-8 -*-
import sys
import threading

from MazeMainWindowUI import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow, QApplication


class MazeMainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MazeMainWindow, self).__init__()
		self.setupUi(self)
		self.centralwidget.parent().resize(800, 600)
		self.widget_mazeDisplayMain.mazeData.size = self.spinBox_mazeSize.value()
		self.widget_mazeDisplayMain.mazeData.initMaze()

	def mainFunc_generatorRun(self):
		self.widget_mazeDisplayMain.runNewGenerator(
			self.comboBox_selectGenerateMethod.currentIndex(),
			self.spinBox_mazeSize.value())


if __name__ == "__main__":
	sys.setrecursionlimit(10000)
	threading.stack_size(128*1024*1024)
	app = QApplication(sys.argv)
	label = MazeMainWindow()
	label.show()
	sys.exit(app.exec_())
