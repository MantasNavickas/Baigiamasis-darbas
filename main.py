from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import sys

class MainWindow(QtWidgets.QMainWindow):  
    def __init__(self):
        super().__init__()
        self.setupUi()

        
        self.subprocesses = {}  
        self.timers = {}  

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(314, 460)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 70, 241, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 120, 241, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 181, 16))
        self.label.setObjectName("label")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(self.open_user_data)
        self.pushButton_2.clicked.connect(self.open_tax_data)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "SB \"EŽERĖLIS\""))
        self.pushButton.setText(_translate("MainWindow", "Bendrijos narių info"))
        self.pushButton_2.setText(_translate("MainWindow", "Bendrijos nario mokesčių info"))
        self.label.setText(_translate("MainWindow", "Sveiki, pasirinkite norimą kategoriją:"))

    def open_user_data(self):
        self.open_subprocess("user_data.py")

    def open_tax_data(self):
        self.open_subprocess("tax_info.py")

    def open_subprocess(self, script_name):
        
        if script_name in self.subprocesses and self.subprocesses[script_name].poll() is None:
            print(f"{script_name} jau veikia, neatidaroma dar kartą.")
            return  

        try:
            process = subprocess.Popen(["python", script_name])
            self.subprocesses[script_name] = process
            
            
            timer = QtCore.QTimer(self)
            timer.timeout.connect(lambda: self.cleanup_process(script_name))
            timer.start(1000)  

            self.timers[script_name] = timer  
        except Exception as e:
            print(f"Klaida paleidžiant {script_name}: {e}")

    def cleanup_process(self, script_name):
        
        process = self.subprocesses.get(script_name)
        if process and process.poll() is not None:  
            self.subprocesses.pop(script_name, None)  
            timer = self.timers.pop(script_name, None)  
            if timer:
                timer.stop()

    def closeEvent(self, event):
        
        for script_name, process in self.subprocesses.items():
            if process.poll() is None:  
                process.terminate() 
        self.subprocesses.clear() 
        event.accept()  


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
