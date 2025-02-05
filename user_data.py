from functions import Function
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(387, 357)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 371, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.button_cancel = QtWidgets.QPushButton(self.tab)
        self.button_cancel.setGeometry(QtCore.QRect(200, 280, 75, 23))
        self.button_cancel.setObjectName("button_cancel")
        self.label_surname = QtWidgets.QLabel(self.tab)
        self.label_surname.setGeometry(QtCore.QRect(40, 80, 47, 13))
        self.label_surname.setObjectName("label_surname")
        self.label_phone = QtWidgets.QLabel(self.tab)
        self.label_phone.setGeometry(QtCore.QRect(40, 170, 47, 13))
        self.label_phone.setObjectName("label_phone")
        self.label_address = QtWidgets.QLabel(self.tab)
        self.label_address.setGeometry(QtCore.QRect(40, 110, 47, 13))
        self.label_address.setObjectName("label_address")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 170, 201, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.button_accept = QtWidgets.QPushButton(self.tab)
        self.button_accept.setGeometry(QtCore.QRect(70, 280, 75, 23))
        self.button_accept.setObjectName("button_accept")
        self.label_name = QtWidgets.QLabel(self.tab)
        self.label_name.setGeometry(QtCore.QRect(40, 50, 47, 13))
        self.label_name.setObjectName("label_name")
        self.label_email = QtWidgets.QLabel(self.tab)
        self.label_email.setGeometry(QtCore.QRect(40, 140, 47, 13))
        self.label_email.setObjectName("label_email")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 140, 201, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 80, 201, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 110, 201, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_title = QtWidgets.QLabel(self.tab)
        self.label_title.setGeometry(QtCore.QRect(20, 10, 291, 21))
        self.label_title.setTextFormat(QtCore.Qt.AutoText)
        self.label_title.setObjectName("label_title")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(30, 210, 321, 51))
        self.groupBox.setObjectName("groupBox")
        self.box_send_sms = QtWidgets.QCheckBox(self.groupBox)
        self.box_send_sms.setGeometry(QtCore.QRect(180, 20, 70, 17))
        self.box_send_sms.setObjectName("box_send_sms")
        self.box_send_email = QtWidgets.QCheckBox(self.groupBox)
        self.box_send_email.setGeometry(QtCore.QRect(40, 20, 70, 17))
        self.box_send_email.setCheckable(True)
        self.box_send_email.setChecked(False)
        self.box_send_email.setObjectName("box_send_email")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bendrijos narių informacija"))
        self.button_cancel.setText(_translate("Dialog", "Atšaukti"))
        self.label_surname.setText(_translate("Dialog", "Pavardė"))
        self.label_phone.setText(_translate("Dialog", "Tel.nr."))
        self.label_address.setText(_translate("Dialog", "Adresas"))
        self.button_accept.setText(_translate("Dialog", "Pridėti"))
        self.label_name.setText(_translate("Dialog", "Vardas"))
        self.label_email.setText(_translate("Dialog", "El.paštas"))
        self.label_title.setText(_translate("Dialog", "Pridėti naują narį:"))
        self.groupBox.setTitle(_translate("Dialog", "Sutinka gauti naujienas:"))
        self.box_send_sms.setText(_translate("Dialog", "SMS žinute"))
        self.box_send_email.setText(_translate("Dialog", "El. paštu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Pridėti"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))

   
   
    def email_box_state(self, state):
        if state == 2:  # Qt.Checked = 2
            return True
        else:
            return False

    def sms_box_state(self, state):
        if state == 2:  # Qt.Checked = 2
            return True
        else:
            return False

    def add_data_to_db(self):
        name = self.lineEdit.text()
        surname = self.lineEdit_2.text ()
        address = self.lineEdit_3.tetx()
        email = self.lineEdit_4.text()
        phone = self.lineEdit_5.text()
        email_news = Ui_Dialog.email_box_state()
        sms_news = Ui_Dialog.sms_box_state()
        status = Function.add_member_data(member_name=name, member_surname=surname, member_address=address, member_email=email, member_phone=phone, send_email=email_news, send_sms=sms_news)
        print(status)
   
   
   
   
   
    # Priskiriame mygtukams funkcijas
        self.button_accept.clicked(self.add_data_to_db)
        self.button_cancel.clicked.connect(self.close)
        self.box_send_email.stateChanged.connect(self.email_box_state)
        self.box_send_sms.stateChanged.connect(self.sms_box_state)

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
