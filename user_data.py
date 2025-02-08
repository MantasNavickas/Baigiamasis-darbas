from functions import Function
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


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
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 170, 171, 20))
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

        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(120, 170, 31, 16))
        self.label.setObjectName("label")

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.button_get_list = QtWidgets.QPushButton(self.tab_2)
        self.button_get_list.setGeometry(QtCore.QRect(40, 62, 281, 151))
        self.button_get_list.setObjectName("button_get_list")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(80, 40, 211, 22))
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")

        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 47, 13))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 47, 13))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(100, 100, 47, 13))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(190, 100, 47, 13))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(290, 100, 47, 13))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 81, 16))
        self.label_7.setObjectName("label_7")

        self.check_email = QtWidgets.QCheckBox(self.tab_3)
        self.check_email.setGeometry(QtCore.QRect(100, 160, 70, 17))
        self.check_email.setObjectName("check_email")

        self.check_sms = QtWidgets.QCheckBox(self.tab_3)
        self.check_sms.setGeometry(QtCore.QRect(220, 160, 70, 17))
        self.check_sms.setObjectName("check_sms")

        self.lineEdit_name = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_name.setGeometry(QtCore.QRect(0, 120, 81, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")

        self.lineEdit_surname = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_surname.setGeometry(QtCore.QRect(80, 120, 81, 20))
        self.lineEdit_surname.setObjectName("lineEdit_surname")

        self.lineEdit_email = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_email.setGeometry(QtCore.QRect(160, 120, 111, 20))
        self.lineEdit_email.setObjectName("lineEdit_email")

        self.lineEdit_phone = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_phone.setGeometry(QtCore.QRect(300, 120, 61, 20))
        self.lineEdit_phone.setObjectName("lineEdit_phone")

        self.button_update = QtWidgets.QPushButton(self.tab_3)
        self.button_update.setGeometry(QtCore.QRect(110, 220, 141, 23))
        self.button_update.setObjectName("button_update")

        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(270, 120, 31, 16))
        self.label_10.setObjectName("label_10")

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")

        self.pushButton_search = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_search.setGeometry(QtCore.QRect(130, 150, 75, 23))
        self.pushButton_search.setObjectName("pushButton_search")

        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 47, 13))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label_9.setObjectName("label_9")

        self.label_search_address = QtWidgets.QLabel(self.tab_4)
        self.label_search_address.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.label_search_address.setObjectName("label_search_address")

        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(20, 90, 47, 13))
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(20, 110, 47, 13))
        self.label_12.setObjectName("label_12")

        self.lineEdit_search_name = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_search_name.setGeometry(QtCore.QRect(110, 30, 221, 20))
        self.lineEdit_search_name.setObjectName("lineEdit_search_name")

        self.lineEdit_search_surname = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_search_surname.setGeometry(QtCore.QRect(110, 50, 221, 20))
        self.lineEdit_search_surname.setObjectName("lineEdit_search_surname")

        self.lineEdit_search_address = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_search_address.setGeometry(QtCore.QRect(110, 70, 221, 20))
        self.lineEdit_search_address.setObjectName("lineEdit_search_address")

        self.lineEdit_search_email = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_search_email.setGeometry(QtCore.QRect(110, 90, 221, 20))
        self.lineEdit_search_email.setObjectName("lineEdit_search_email")

        self.lineEdit_search_phone = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_search_phone.setGeometry(QtCore.QRect(140, 110, 191, 20))
        self.lineEdit_search_phone.setObjectName("lineEdit_search_phone")

        self.textEdit_found_contacts = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_found_contacts.setEnabled(False)
        self.textEdit_found_contacts.setGeometry(QtCore.QRect(10, 200, 341, 71))
        self.textEdit_found_contacts.setObjectName("textEdit_found_contacts")

        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(110, 110, 31, 16))
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)

        Dialog.setTabOrder(self.lineEdit, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        Dialog.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        Dialog.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        Dialog.setTabOrder(self.lineEdit_5, self.box_send_email)
        Dialog.setTabOrder(self.box_send_email, self.box_send_sms)
        Dialog.setTabOrder(self.box_send_sms, self.button_accept)
        Dialog.setTabOrder(self.button_accept, self.button_cancel)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Assigning functions to buttons
        # tab 1
        self.button_accept.clicked.connect(self.add_data_to_db)
        self.button_cancel.clicked.connect(Dialog.close)
        self.box_send_email.stateChanged.connect(self.email_box_state)
        self.box_send_sms.stateChanged.connect(self.sms_box_state)
        # tab 2
        self.button_get_list.clicked.connect(self.get_member_list)
        # tab 3
        self.button_update.clicked.connect(self.update_data)
        # tab 4
        self.pushButton_search.clicked.connect(self.search)

        # Keyboard shortcuts
        self.button_accept.setShortcut(QtCore.Qt.Key_Return)
        self.button_accept.setShortcut(QtCore.Qt.Key_Enter)
        self.button_cancel.setShortcut(QtCore.Qt.Key_Escape)

        # combo box
        self.load_addresses()
        self.comboBox.currentIndexChanged.connect(self.fill_user_data)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bendrijos narių informacija"))
        # tab 1
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
        self.label.setText(_translate("dialog_user_data", "+370"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Pridėti"))
        # tab 2
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("dialog_user_data", "Narių sąrašas"))
        self.button_get_list.setText(_translate("dialog_user_data", "Gauti bendrijos narių sąrašą"))
        # tab 3
        self.label_2.setText(_translate("dialog_user_data", "Adresas"))
        self.label_3.setText(_translate("dialog_user_data", "Vardas"))
        self.label_4.setText(_translate("dialog_user_data", "Pavardė"))
        self.label_5.setText(_translate("dialog_user_data", "El.paštas"))
        self.label_6.setText(_translate("dialog_user_data", "Tel.nr."))
        self.label_7.setText(_translate("dialog_user_data", "Info siunčiama:"))
        self.check_email.setText(_translate("dialog_user_data", "El. paštu"))
        self.check_sms.setText(_translate("dialog_user_data", "SMS"))
        self.button_update.setText(_translate("dialog_user_data", "Atnaujinti duomenis"))
        self.label_10.setText(_translate("dialog_user_data", "+370"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("dialog_user_data", "Atnaujinti duomenis"))
        # tab 4
        self.pushButton_search.setText(_translate("dialog_user_data", "Ieškoti"))
        self.label_8.setText(_translate("dialog_user_data", "Vardas"))
        self.label_9.setText(_translate("dialog_user_data", "Pavardė"))
        self.label_search_address.setText(_translate("dialog_user_data", "Adresas"))
        self.label_11.setText(_translate("dialog_user_data", "El.paštas"))
        self.label_12.setText(_translate("dialog_user_data", "Tel.nr."))
        self.label_13.setText(_translate("dialog_user_data", "+370"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("dialog_user_data", "Paieška"))



    def email_box_state(self, state):
        return state == 2  # Qt.Checked = 2

    def sms_box_state(self, state):
        return state == 2  # Qt.Checked = 2

    def add_data_to_db(self):
        name = self.lineEdit.text()
        surname = self.lineEdit_2.text()
        address = self.lineEdit_3.text()
        email = self.lineEdit_4.text()
        phone = self.lineEdit_5.text()
        email_news = self.box_send_email.isChecked()
        sms_news = self.box_send_sms.isChecked()
        
        f_obj = Function(
            member_name=name, 
            member_surname=surname, 
            member_address=address, 
            member_email=email, 
            member_phone=phone, 
            send_email=email_news, 
            send_sms=sms_news
        )
        
        status = f_obj.add_member_data()
        self.show_info_dialog(status)

        # Clear input fields after adding data
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.box_send_email.setChecked(False)
        self.box_send_sms.setChecked(False)

    def show_info_dialog(self, message):
        dialog = QtWidgets.QMessageBox()
        dialog.setIcon(QtWidgets.QMessageBox.Information)
        dialog.setText(message)
        dialog.setWindowTitle("Informacija")
        dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        dialog.button(QtWidgets.QMessageBox.Ok).setShortcut(QtCore.Qt.Key_Return)
        dialog.exec_()

    def get_member_list(self):
        g_list = Function(
            member_name='', 
            member_surname='', 
            member_address='', 
            member_email='', 
            member_phone='', 
            send_email='', 
            send_sms=''
        )
        g_list.show_member_list(output='list.xlsx')
        status = g_list.show_member_list(output='list.xlsx')
        self.show_info_dialog(status)
    
    
    def load_addresses(self):
        try:
            with sqlite3.connect("SB_Ezerelis.db") as conn:
                cursor = conn.cursor()

                # Fetch all unique addresses from the database and sort them
                cursor.execute("SELECT DISTINCT Adresas FROM sb_nariai ORDER BY Adresas ASC")
                addresses = [row[0] for row in cursor.fetchall()]  # Extracting values from tuples

                # Clear and populate combo box with sorted addresses
                self.comboBox.clear()
                self.comboBox.addItem("Pasirinkti adresą")  # Add a placeholder at the start
                self.comboBox.addItems(addresses)

            # Optionally, set the current text to the placeholder, if not already set
            self.comboBox.setCurrentText("Pasirinkti adresą")

        except sqlite3.Error as e:
            self.show_info_dialog(f"Database error: {e}")

    
    def fill_user_data(self):
        selected_address = self.comboBox.currentText() # Get selected address from combo box
        
        if selected_address == "Pasirinkti adresą":
            # Clear all lineEdits
            self.lineEdit_name.clear()
            self.lineEdit_surname.clear()
            self.lineEdit_email.clear()
            self.lineEdit_phone.clear()

            # Uncheck the checkboxes
            self.check_email.setChecked(False)
            self.check_sms.setChecked(False)

            return  # Do nothing else if placeholder is selected

        if not selected_address:  # If no address is selected, do nothing
            return

        try:
            # Connect to SQLite database using "with" to ensure automatic closing
            with sqlite3.connect("SB_Ezerelis.db") as conn:
                cursor = conn.cursor()

                # Fetch user data based on the selected address
                cursor.execute(
                    "SELECT Vardas, Pavardė, El_paštas, Tel_nr, El_laiškai, SMS FROM sb_nariai WHERE Adresas = ?",
                    (selected_address,),
                )
                result = cursor.fetchone()  # Fetch one record
                print(result)
               

            # If data exists, populate fields
            if result:
                name, surname, email, phone, send_email, send_sms = result

                self.lineEdit_name.setText(name)
                self.lineEdit_surname.setText(surname)
                self.lineEdit_email.setText(email)
                self.lineEdit_phone.setText(phone)

                self.check_email.setChecked(bool(send_email))  
                self.check_sms.setChecked(bool(send_sms))  

        except sqlite3.Error as e:
            self.show_info_dialog(f"Database error: {e}")
    

    def update_data(self):
        
        name = self.lineEdit_name.text()
        surname = self.lineEdit_surname.text()
        address = self.comboBox.currentText()
        email = self.lineEdit_email.text()
        phone = self.lineEdit_phone.text()
        news_email = self.check_email.isChecked()
        news_sms = self.check_sms.isChecked()

        news_email = bool(news_email)  # Ensures it's a boolean
        news_sms = bool(news_sms)  # Ensures it's a boolean
        
        data = Function(
            member_name=name, 
            member_surname=surname, 
            member_address=address, 
            member_email=email, 
            member_phone=phone, 
            send_email=news_email, 
            send_sms=news_sms
        )
        
        print(news_email)
        print(news_sms)
        data.modify_member()
        status = data.modify_member()
        self.show_info_dialog(status)
    
    def search(self):
        name = self.lineEdit_search_name.text()
        surname = self.lineEdit_search_surname.text()
        address = self.lineEdit_search_address.text()
        email = self.lineEdit_search_email.text()
        phone = self.lineEdit_search_phone.text()

        # Create the Function object to perform the search
        search_data = Function(
            member_name=name,
            member_surname=surname,
            member_address=address,
            member_email=email,
            member_phone=phone,
            send_email="",
            send_sms=""
        )

        # Perform the search using the Function's method
        data_found = search_data.search_member()

        if isinstance(data_found, str):  # Handles error messages
            self.textEdit_found_contacts.setText(data_found)
        else:
            data = "\n".join([" | ".join(map(str, member)) for member in data_found])
            self.textEdit_found_contacts.setText(data)
        

        





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())