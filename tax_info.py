from functions import Function_set
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Dialog(object):

    def __init__(self):
        super().__init__()
        self.function = Function_set('', '', '', '', '', '', '') 
        self.run_add_member_tax_info()  

    def run_add_member_tax_info(self):
        result = self.function.add_member_tax_info()  
        print(result)  


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 371, 81))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 331, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 371, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(120, 30, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 30, 101, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 80, 71, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 80, 61, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 120, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(90, 60, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(180, 60, 81, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(260, 80, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(260, 60, 81, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

         # combo box
        self.load_addresses()
        self.add_payment_methods()
        self.comboBox.currentIndexChanged.connect(self.fill_user_data)

        self.pushButton_2.clicked.connect(self.update_payment_info)
        self.pushButton.clicked.connect(self.get_tax_list)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Mokesčių info"))
        self.groupBox.setTitle(_translate("Dialog", "Sąrašo peržiūra:"))
        self.pushButton.setText(_translate("Dialog", "Mokesčio mokėjimo lentelė .xlsx formatu"))
        self.groupBox_2.setTitle(_translate("Dialog", "Naujų duomenų pridėjimas:"))
        self.label.setText(_translate("Dialog", "Mokėtojo adresas:"))
        self.pushButton_2.setText(_translate("Dialog", "Pridėti duomenis"))
        self.label_2.setText(_translate("Dialog", "Vardas"))
        self.label_3.setText(_translate("Dialog", "Pavardė"))
        self.label_4.setText(_translate("Dialog", "Mokėjimo suma"))
        self.label_5.setText(_translate("Dialog", "Mokėjimo būdas"))
        

    def show_info_dialog(self, message):
        dialog = QtWidgets.QMessageBox()
        dialog.setIcon(QtWidgets.QMessageBox.Information)
        dialog.setText(message)
        dialog.setWindowTitle("Informacija")
        dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        dialog.button(QtWidgets.QMessageBox.Ok).setShortcut(QtCore.Qt.Key_Return)
        dialog.exec_()


    def load_addresses(self):
        try:
            with sqlite3.connect("SB_Ezerelis.db") as conn:
                cursor = conn.cursor()

                
                cursor.execute(
                    "SELECT DISTINCT Adresas FROM nario_mokestis ORDER BY Adresas ASC"
                )
                addresses = [
                    row[0] for row in cursor.fetchall()
                ]  

                
                self.comboBox.clear()
                self.comboBox.addItem(
                    "Pasirinkti adresą"
                )  
                self.comboBox.addItems(addresses)

                
                self.comboBox.setCurrentText("Pasirinkti adresą")

        except sqlite3.Error as e:
                self.show_info_dialog(f"Database error: {e}")
    
    def fill_user_data(self):
        selected_address = (
            self.comboBox.currentText()
        )  

        if selected_address == "Pasirinkti adresą":
            
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            
            return  

        if not selected_address:  
            return

        try:
            
            with sqlite3.connect("SB_Ezerelis.db") as conn:
                cursor = conn.cursor()

                
                cursor.execute(
                    "SELECT Vardas, Pavardė FROM nario_mokestis WHERE Adresas = ?",
                    (selected_address,),
                )
                result = cursor.fetchone()  
                print(result)

            
            if result:
                name, surname = result

                self.lineEdit.setText(name)
                self.lineEdit_2.setText(surname)
                
        except sqlite3.Error as e:
            self.show_info_dialog(f"Database error: {e}")
    
    def add_payment_methods(self):
        methods = ['Grynaisiais', 'Pavedimu']
        self.comboBox_2.addItems(methods)


    def update_payment_info(self):

        is_payed = self.lineEdit_3.text().strip()
        addres_text = self.comboBox.currentText()        
        if is_payed and addres_text != "Pasirinkti adresą":
            f = self.function
            payed = self.lineEdit_3.text()
            method = self.comboBox_2.currentText()
            address = self.comboBox.currentText()
            status = f.add_tax_payment_info(payed_total=payed, method=method, address=address)        
            self.show_info_dialog(status)
            log_string = f'Pridėtas naujas mokėjimas: {address}, {payed}, {method}'
            f.add_log(log_string)
            self.lineEdit_3.clear()
            self.comboBox.setCurrentText("Pasirinkti adresą")
            f.add_member_tax_info()
            
        else:
            status = 'Mokėjimo sumos laukelis tuščias, arba nepasirintas joks adresas'
            self.show_info_dialog(status)
        
    def get_tax_list(self):

        output = 'nario_mokestis.xlsx'
        f = self.function        
        status = f.show_tax_list(output)
        log_string = f'Sugeneruotas failas {output}'
        f.add_log(log_string)
        self.show_info_dialog(status)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

