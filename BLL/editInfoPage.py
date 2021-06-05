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
import infoEdit

class Main(QtWidgets.QMainWindow, infoEdit.Ui_editPatient):
	def __init__(self):
		super(Main, self).__init__()
		self.setupUi(self)
		self.IDList = dh.getPatientIDList()
		self.id = 0

		self.IDMap = {}

		self.patientEdit_combo.addItem("--Select Patient--")
		for x in self.IDList:
			self.patientEdit_combo.addItem("Patient "+str(x))
			self.IDMap["Patient "+str(x)] = x

		self.patientEdit_combo.activated.connect(self.showPatientInfo)
		self.saveInfo_btn.clicked.connect(self.updateInfo)

	def showPatientInfo(self):
		try:
			self.current_choice = ""
			self.current_choice = self.patientEdit_combo.currentText()
			self.id = self.IDMap[self.current_choice]

			self.info = dh.getPatientINFO(self.id)
			self.nameEdit_blank.setText(str(self.info[0]))
			self.classEdit_blank.setText(str(self.info[1]))
			self.ageEdit_blank.setText(str(self.info[2]))
			self.heightEdit_blank.setText(str(self.info[3]))
			self.weightEdit_blank.setText(str(self.info[4]))
		except:
			print("invalid selection")

	def updateInfo(self):
		self.newName = self.nameEdit_blank.text()
		self.newClass = self.classEdit_blank.text()
		self.newAge = self.ageEdit_blank.text()
		self.newHeight = self.heightEdit_blank.text()
		self.newWeight = self.weightEdit_blank.text()

		dh.editPatientName(self.id,self.newName)
		dh.editPatientClass(self.id,self.newClass)
		dh.editPatientAge(self.id,self.newAge)
		dh.editPatientHeight(self.id,self.newHeight)
		dh.editPatientWeight(self.id,self.newWeight)

		if(self.id == 0):
			print("nothing to save")
		else:
			msg = QMessageBox()
			msg.setWindowTitle("SUCCESS")
			msg.setText("Patient "+str(self.id)+" updated!")
			msg.setIcon(QMessageBox.Information)
			x = msg.exec_()
        

    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())