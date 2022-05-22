from PyQt5 import QtWidgets,QtGui,QtCore,Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
import sys
import serial

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(100, 100, 1600, 900)
        self.setWindowTitle("TAU-SAT Yer İstasyonu")
        self.initUI()
        self.timer_status=QTimer(self)
        self.timer_status.timeout.connect(lambda: self.Update())
        self.timer_status.start(1000)

    def initUI(self):
        self.Serial_Port=QtWidgets.QLabel(self)
        self.Serial_Port.setGeometry(300,300,300,300)

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 221, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)

        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 3, 0, 1, 1)

        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)

        self.pushButton.setText("Başlat")
        self.pushButton_2.setText("Ayrıl")
        self.pushButton_3.setText("Motorları Aç")
        self.pushButton_4.setText("Motorları Kapat")
        self.pushButton_5.setText("Video Seç")
        self.pushButton_6.setText("Video Gönder")
        self.pushButton_7.setText("Kalibrasyon")
        self.pushButton_8.setText("Asenkron Video")


        
    def Update(self):
        pass
        # self.Serial_Port.setText("Sicaklik Degeri "+str(ser.read_until(size=5)))

def window():
    app= QApplication(sys.argv)
    win= Window()
    win.show()
    win.Update()
    sys.exit(app.exec_())

# ser = serial.Serial("COM5","9600")
window()
