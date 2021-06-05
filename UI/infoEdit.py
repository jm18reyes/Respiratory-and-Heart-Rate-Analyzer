# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infoEdit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editPatient(object):
    def setupUi(self, editPatient):
        editPatient.setObjectName("editPatient")
        editPatient.resize(445, 560)
        self.centralwidget = QtWidgets.QWidget(editPatient)
        self.centralwidget.setObjectName("centralwidget")
        self.patientEdit_combo = QtWidgets.QComboBox(self.centralwidget)
        self.patientEdit_combo.setGeometry(QtCore.QRect(110, 20, 231, 41))
        self.patientEdit_combo.setObjectName("patientEdit_combo")
        self.nameEdit_blank = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit_blank.setGeometry(QtCore.QRect(20, 100, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setBold(True)
        font.setWeight(75)
        self.nameEdit_blank.setFont(font)
        self.nameEdit_blank.setText("")
        self.nameEdit_blank.setObjectName("nameEdit_blank")
        self.nameEdit_blank.setPlaceholderText("Name")
        self.ageEdit_blank = QtWidgets.QLineEdit(self.centralwidget)
        self.ageEdit_blank.setGeometry(QtCore.QRect(20, 220, 171, 41))
        self.ageEdit_blank.setFont(font)
        self.ageEdit_blank.setText("")
        self.ageEdit_blank.setObjectName("ageEdit_blank")
        self.ageEdit_blank.setPlaceholderText("Age")
        self.classEdit_blank = QtWidgets.QLineEdit(self.centralwidget)
        self.classEdit_blank.setGeometry(QtCore.QRect(20, 160, 321, 41))
        self.classEdit_blank.setFont(font)
        self.classEdit_blank.setText("")
        self.classEdit_blank.setObjectName("classEdit_blank")
        self.classEdit_blank.setPlaceholderText("Classification")
        self.heightEdit_blank = QtWidgets.QLineEdit(self.centralwidget)
        self.heightEdit_blank.setGeometry(QtCore.QRect(20, 280, 171, 41))
        self.heightEdit_blank.setFont(font)
        self.heightEdit_blank.setText("")
        self.heightEdit_blank.setObjectName("heightEdit_blank")
        self.heightEdit_blank.setPlaceholderText("Height")
        self.weightEdit_blank = QtWidgets.QLineEdit(self.centralwidget)
        self.weightEdit_blank.setGeometry(QtCore.QRect(20, 340, 171, 41))
        self.weightEdit_blank.setFont(font)
        self.weightEdit_blank.setText("")
        self.weightEdit_blank.setObjectName("weightEdit_blank")
        self.weightEdit_blank.setPlaceholderText("Weight")
        self.saveInfo_btn = QtWidgets.QPushButton(self.centralwidget)
        self.saveInfo_btn.setGeometry(QtCore.QRect(150, 430, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.saveInfo_btn.setFont(font)
        self.saveInfo_btn.setStyleSheet("background-color: rgb(146, 208, 80);")
        self.saveInfo_btn.setObjectName("saveInfo_btn")
        editPatient.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(editPatient)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 445, 26))
        self.menubar.setObjectName("menubar")
        editPatient.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(editPatient)
        self.statusbar.setObjectName("statusbar")
        editPatient.setStatusBar(self.statusbar)

        self.retranslateUi(editPatient)
        QtCore.QMetaObject.connectSlotsByName(editPatient)

    def retranslateUi(self, editPatient):
        _translate = QtCore.QCoreApplication.translate
        editPatient.setWindowTitle(_translate("editPatient", "EDIT INFORMATION"))
        self.saveInfo_btn.setText(_translate("editPatient", "SAVE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editPatient = QtWidgets.QMainWindow()
    ui = Ui_editPatient()
    ui.setupUi(editPatient)
    editPatient.show()
    sys.exit(app.exec_())
