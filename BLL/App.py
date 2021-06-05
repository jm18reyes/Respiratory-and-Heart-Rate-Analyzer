from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import sys
import csv 
import matplotlib.pyplot as plt
import numpy as np


import patientPage
import editInfoPage
import editValuePage

sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../patient.db')


sys.path.insert(0, '../UI')
import homepage

class Main(QtWidgets.QMainWindow, homepage.Ui_Homepage):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.upload_btn.clicked.connect(self.showDialogBox)
        self.patientData_btn.clicked.connect(self.showPatientPage)
        self.editInfo_btn.clicked.connect(self.showEditPage)
        self.resetDatabase_btn.clicked.connect(self.clearDatabase)
        self.editValues_btn.clicked.connect(self.showEditValuePage)

        self.patient = {}
        self.listHolder = []

        self.breathList = []
        self.heartList = []
        self.minuteList = []

        self.newPatient = True

    def showEditValuePage(self):
        self.newWin = editValuePage.Main()
        self.newWin.show()

    def clearDatabase(self):
        

        reply = QMessageBox.question(self, 'Warning!', 'Are you sure you want to clear database?', QMessageBox.Yes, QMessageBox.No)
        if (reply == QMessageBox.Yes):
            dh.resetDatabase()
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Database is cleared")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Notice")
            msg.setText("Operation Aborted")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
    def showDialogBox(self):
        try:

            self.filename = QFileDialog.getOpenFileName()
            print(self.filename[0])
            self.readTextFile(self.filename[0])
            msg = QMessageBox()
            msg.setWindowTitle("SUCCESS")
            msg.setText("FILE UPLOADED")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Oops")
            msg.setText("No file selected")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

    def readTextFile(self,filePath):
        self.currentPatient = 0
        self.currentDataCount = 0
        self.databaseDataCount = 0
        with open(filePath, newline='') as csvfile:
            f = csv.reader(csvfile,delimiter = ',')
            print("Opened")
            for i in f:
                self.currentDataCount += 1
                if(int(i[-1]) == 1):
                    self.currentPatient +=1
                    self.listHolder = []
                    self.listHolder.append(i)
                else:
                    self.listHolder.append(i)

                self.patient[str(self.currentPatient)] = self.listHolder

            self.startPatient = 1 #int(self.checkLatestData())

            self.databaseDataCount = dh.getDataCount()


            print("Current DataCount: "+str(self.currentDataCount))
            print("Database DataCount: "+str(self.databaseDataCount))
            print("startPatient: "+str(self.startPatient))
            print("currentPatient: "+str(self.currentPatient))
            print(self.patient)

            
            self.latestIDFromBackup = dh.getLatestIDFromBackup()
            
            dh.safeClean()
            for j in range(self.startPatient,self.currentPatient+1):
                #print(patient[str(j)])

                dh.initializePatient(j)
                dh.initializeResult(j)

                if(j in dh.getPatientBackupIDList()):
                    print("nothing")
                else:
                    dh.initializePatientBackup(j)
                    dh.initializeResultBackup(j)


                for k in self.patient[str(j)]:
                    print(k)

                    self.bVal = int(k[0])
                    self.hVal = int(k[2])
                    self.mVal = int(k[-1])

                    self.breathList.append(self.bVal)
                    self.heartList.append(self.hVal)
                    self.minuteList.append(self.mVal)

                    print("Saved: "+str(self.bVal)+" "+str(self.hVal)+" "+str(self.mVal))

                    dh.insertData(j,self.bVal,self.hVal,self.mVal)


            #dh.prepareBackup()
            dh.restoreFromBackup()

            

    def checkLatestData(self):
        latestID = dh.getLatestID()
        if(latestID is None):
            return 1
        else:
            return latestID

    def showPatientPage(self):
        print("hello")
        if(dh.getLatestID() is None):
            msg = QMessageBox()
            msg.setWindowTitle("Oops")
            msg.setText("No patient in database yet")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            self.newWin = patientPage.Main()
            self.newWin.show()

    def showEditPage(self):
        print("hello")
        if(dh.getLatestID() is None):
            msg = QMessageBox()
            msg.setWindowTitle("Oops")
            msg.setText("No patient in database yet")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            self.newWin = editInfoPage.Main()
            self.newWin.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())