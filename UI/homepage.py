# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Homepage(object):
    def setupUi(self, Homepage):
        Homepage.setObjectName("Homepage")
        Homepage.resize(531, 556)
        self.centralwidget = QtWidgets.QWidget(Homepage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 501, 151))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-image : url(image.png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.upload_btn = QtWidgets.QPushButton(self.centralwidget)
        self.upload_btn.setGeometry(QtCore.QRect(100, 180, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.upload_btn.setFont(font)
        self.upload_btn.setAutoFillBackground(False)
        self.upload_btn.setStyleSheet("background-color:rgb(146, 208, 80)")
        self.upload_btn.setObjectName("upload_btn")
        self.patientData_btn = QtWidgets.QPushButton(self.centralwidget)
        self.patientData_btn.setGeometry(QtCore.QRect(100, 260, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.patientData_btn.setFont(font)
        self.patientData_btn.setAutoFillBackground(False)
        self.patientData_btn.setStyleSheet("background-color:rgb(146, 208, 80)")
        self.patientData_btn.setObjectName("patientData_btn")
        self.editInfo_btn = QtWidgets.QPushButton(self.centralwidget)
        self.editInfo_btn.setGeometry(QtCore.QRect(100, 340, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.editInfo_btn.setFont(font)
        self.editInfo_btn.setAutoFillBackground(False)
        self.editInfo_btn.setStyleSheet("background-color:rgb(146, 208, 80)")
        self.editInfo_btn.setObjectName("editInfo_btn")
        self.resetDatabase_btn = QtWidgets.QPushButton(self.centralwidget)
        self.resetDatabase_btn.setGeometry(QtCore.QRect(10, 450, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.resetDatabase_btn.setFont(font)
        self.resetDatabase_btn.setAutoFillBackground(False)
        self.resetDatabase_btn.setStyleSheet("background-color:rgb(154, 0, 0);\n"
"color: rgb(255, 255, 255)")
        self.resetDatabase_btn.setObjectName("resetDatabase_btn")
        self.editValues_btn = QtWidgets.QPushButton(self.centralwidget)
        self.editValues_btn.setGeometry(QtCore.QRect(390, 450, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.editValues_btn.setFont(font)
        self.editValues_btn.setAutoFillBackground(False)
        self.editValues_btn.setStyleSheet("background-color:rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255)")
        self.editValues_btn.setObjectName("editValues_btn")
        Homepage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Homepage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 26))
        self.menubar.setObjectName("menubar")
        Homepage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Homepage)
        self.statusbar.setObjectName("statusbar")
        Homepage.setStatusBar(self.statusbar)

        self.retranslateUi(Homepage)
        QtCore.QMetaObject.connectSlotsByName(Homepage)

    def retranslateUi(self, Homepage):
        _translate = QtCore.QCoreApplication.translate
        Homepage.setWindowTitle(_translate("Homepage", "HOME"))
        self.upload_btn.setText(_translate("Homepage", "Upload File"))
        self.patientData_btn.setText(_translate("Homepage", "View Patient Data"))
        self.editInfo_btn.setText(_translate("Homepage", "EDIT PATIENT INFO"))
        self.resetDatabase_btn.setText(_translate("Homepage", "RESET DATABASE"))
        self.editValues_btn.setText(_translate("Homepage", "Edit Values"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Homepage = QtWidgets.QMainWindow()
    ui = Ui_Homepage()
    ui.setupUi(Homepage)
    Homepage.show()
    sys.exit(app.exec_())
