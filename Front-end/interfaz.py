# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazPython.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(689, 716)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(70, 670, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 70, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(20, 160, 31, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(60, 160, 41, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 220, 41, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(60, 220, 31, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 260, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.checkBox_5 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 280, 31, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_6.setGeometry(QtCore.QRect(60, 280, 31, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 320, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.checkBox_7 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 340, 31, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_8.setGeometry(QtCore.QRect(60, 340, 31, 17))
        self.checkBox_8.setObjectName("checkBox_8")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 380, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.checkBox_9 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_9.setGeometry(QtCore.QRect(20, 400, 31, 17))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_10.setGeometry(QtCore.QRect(60, 400, 31, 17))
        self.checkBox_10.setObjectName("checkBox_10")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 100, 181, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(6, 100, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(5, 460, 661, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(290, 430, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Formulario:"))
        self.label_2.setText(_translate("Dialog", "Diagnostico Sistema Respiratorio"))
        self.label_3.setText(_translate("Dialog", "¿Tiene tos persistente?"))
        self.checkBox.setText(_translate("Dialog", "Si"))
        self.checkBox_2.setText(_translate("Dialog", "No"))
        self.label_4.setText(_translate("Dialog", "¿Experimenta dificultad para respirar?"))
        self.checkBox_3.setText(_translate("Dialog", "Si"))
        self.checkBox_4.setText(_translate("Dialog", "No"))
        self.label_5.setText(_translate("Dialog", "¿Ha tenido fiebre recientemente?"))
        self.checkBox_5.setText(_translate("Dialog", "Si"))
        self.checkBox_6.setText(_translate("Dialog", "No"))
        self.label_6.setText(_translate("Dialog", "¿Ha experimentado dolor en el pecho?"))
        self.checkBox_7.setText(_translate("Dialog", "Si"))
        self.checkBox_8.setText(_translate("Dialog", "No"))
        self.label_7.setText(_translate("Dialog", "¿Ha tenido congestión nasal o secreción nasal?"))
        self.checkBox_9.setText(_translate("Dialog", "Si"))
        self.checkBox_10.setText(_translate("Dialog", "No"))
        self.label_8.setText(_translate("Dialog", "Digite su nombre:"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Tos "))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "New Column"))
        self.label_9.setText(_translate("Dialog", "Registro:"))
