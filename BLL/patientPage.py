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
import patientWin

class Main(QtWidgets.QMainWindow, patientWin.Ui_patientDataWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.IDList = dh.getPatientIDList()
        self.id = 0

        self.IDMap = {}

        self.patientList_combo.addItem("--Select Patient--")
        for x in self.IDList:
            self.patientList_combo.addItem("Patient "+str(x))
            self.IDMap["Patient "+str(x)] = x

        self.patientList_combo.activated.connect(self.showPatientInfo)
        self.analysis_btn.clicked.connect(self.showAnalysis)

    def showPatientInfo(self):
        try:
            self.current_choice = ""
            self.current_choice = self.patientList_combo.currentText()
            self.id = self.IDMap[self.current_choice]

            self.info = dh.getPatientINFO(self.id)
            self.name_lbl.setText(str(self.info[0]))
            self.class_lbl.setText(str(self.info[1]))
            self.age_lbl.setText(str(self.info[2]))
            self.height_lbl.setText(str(self.info[3]))
            self.weight_lbl.setText(str(self.info[4]))
        except:
            print("invalid selction")

    def showAnalysis(self):
        if(self.id == 0):
            print("Do Nothing")
        else:
            self.computeAverage(self.id)
            self.analyzeData(self.id)
            self.graphBreath(self.id)

    def computeAverage(self,ID):
        self.bList = dh.getBreathList(ID)
        self.mList = dh.getMinuteList(ID)
        self.hList = dh.getHeartRateList(ID)

        self.breathAverage = max(self.bList)/max(self.mList)

        self.sumHeart = 0
        for i in self.hList:
            self.sumHeart += i
        
        self.heartrateAverage = self.sumHeart/len(self.hList)


        dh.updateAverage(ID,self.breathAverage,self.heartrateAverage)

    def analyzeData(self,ID):

        self.b_ave = dh.getBreathAve(ID)
        self.h_ave = dh.getHeartrateAve(ID)
        self.respiStatus = "Normal"
        self.heartStatus = "Normal"

        self.lowRespi = dh.getLowRespiValues()
        self.highRespi = dh.getHighRespiValues()
        self.lowHeart = dh.getLowHeartValues()
        self.highHeart = dh.getHighHeartValues()

        print(self.lowRespi)
        print(self.highRespi)
        print(self.lowHeart)
        print(self.highHeart)

        if(float(self.b_ave) < float(self.lowRespi[1]) and float(self.b_ave) >= float(self.lowRespi[0])):
            print("Low Respiration Rate")
            self.respiStatus = "Abnormal"
            print("Respiration Rate: "+self.respiStatus)

            dh.updateBreathDiagnosis(ID,self.respiStatus)
        elif(float(self.b_ave) > float(self.highRespi[0]) and float(self.b_ave) <= float(self.highRespi[1])):
            print("High Respiration Rate")
            self.respiStatus = "Abnormal"
            print("Respiration Rate: "+self.respiStatus)

            dh.updateBreathDiagnosis(ID,self.respiStatus)
        else:
            self.respiStatus = "Normal"
            print("Respiration Rate: "+self.respiStatus)

            dh.updateBreathDiagnosis(ID,self.respiStatus)


        if(float(self.h_ave) < float(self.lowHeart[1]) and float(self.h_ave) >= float(self.lowHeart[0])):
            print("Low Heart Rate")
            self.heartStatus = "Abnormal"
            print("Heart Rate: "+self.heartStatus)

            dh.updateHeartDiagnosis(ID,self.heartStatus)
        elif(float(self.h_ave) > float(self.highHeart[0]) and float(self.h_ave) <= float(self.highHeart[1])):
            print("High Heart Rate")
            self.heartStatus = "Abnormal"
            print("Heart Rate: "+self.heartStatus)

            dh.updateHeartDiagnosis(ID,self.heartStatus)
        else:
            self.heartStatus = "Normal"
            print("Heart Rate: "+self.heartStatus)

            dh.updateHeartDiagnosis(ID,self.heartStatus)

    def graphBreath(self,ID):
        self.bList = dh.getBreathList(ID)
        self.mList = dh.getMinuteList(ID)
        self.hList = dh.getHeartRateList(ID)
        self.bDiag = dh.getBreathDiagnosis(ID)
        self.hDiag = dh.getHeartDiagnosis(ID)



        fig,(bGraph,hGraph) = plt.subplots(2)

        mngr = plt.get_current_fig_manager()
        bGraph.plot(self.mList, self.bList,marker='o', markerfacecolor='green', markersize=12)
        bGraph.set_yticks(np.arange(0,self.bList[-1]+10,step=5))


        # giving a title to my graph

        hGraph.plot(self.mList, self.hList,marker='o', markerfacecolor='red', markersize=12)
        hGraph.set_yticks(np.arange(self.hList[-1]-20,self.hList[-1]+30,step=5))

        if(self.bDiag == "Normal" and self.hDiag == "Normal"):
            self.textColor = "green"
        else:
            self.textColor = "red"

        fig.suptitle("Respiratory Rate:" + self.bDiag + "  Heart Rate: " + self.hDiag,color=self.textColor)
        # function to show the plot

        fig.set_figheight(8)
        fig.set_figwidth(8)

        plt.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())