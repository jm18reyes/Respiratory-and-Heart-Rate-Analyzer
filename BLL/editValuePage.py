from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import csv 
import matplotlib.pyplot as plt
import numpy as np



sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../patient.db')


sys.path.insert(0, '../UI')
import valueEdit

class Main(QtWidgets.QMainWindow, valueEdit.Ui_editValues):
	def __init__(self):
		super(Main, self).__init__()
		self.setupUi(self)
		self.saveValues_btn.clicked.connect(self.changeAbnormalityValues)

		self.lowRespi = dh.getLowRespiValues()
		self.highRespi = dh.getHighRespiValues()
		self.lowHeart = dh.getLowHeartValues()
		self.highHeart = dh.getHighHeartValues()

		self.lowRespiMin_blank.setText(str(self.lowRespi[0]))
		self.lowRespiMax_blank.setText(str(self.lowRespi[1]))
		self.highRespiMin_blank.setText(str(self.highRespi[0]))
		self.highRespiMax_blank.setText(str(self.highRespi[1]))
		self.lowHeartMin_blank.setText(str(self.lowHeart[0]))
		self.lowHeartMax_blank.setText(str(self.lowHeart[1]))
		self.highHeartMin_blank.setText(str(self.highHeart[0]))
		self.highHeartMax_blank.setText(str(self.highHeart[1]))



	def changeAbnormalityValues(self):
		try:
			self.rLow_min = int(self.lowRespiMin_blank.text())
			self.rLow_max = int(self.lowRespiMax_blank.text())
			self.rHigh_min = int(self.highRespiMin_blank.text())
			self.rHigh_max = int(self.highRespiMax_blank.text())
			self.hLow_min = int(self.lowHeartMin_blank.text())
			self.hLow_max = int(self.lowHeartMax_blank.text())
			self.hHigh_min = int(self.highHeartMin_blank.text())
			self.hHigh_max = int(self.highHeartMax_blank.text())



			dh.updateRangeForRespi(self.rLow_min,self.rLow_max,self.rHigh_min,self.rHigh_max)
			dh.updateRangeForHeart(self.hLow_min,self.hLow_max,self.hHigh_min,self.hHigh_max)

			msg = QMessageBox()
			msg.setWindowTitle("SUCCESS")
			msg.setText("Values are now updated!")
			msg.setIcon(QMessageBox.Information)
			x = msg.exec_()
		except:
			msg = QMessageBox()
			msg.setWindowTitle("Error!")
			msg.setText("Input is invalid!")
			msg.setIcon(QMessageBox.Critical)
			x = msg.exec_()

	
        

    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())