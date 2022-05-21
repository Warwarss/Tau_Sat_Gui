from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import serial
import time

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(100, 100, 1600, 900)
        self.setWindowTitle("TAU-SAT Yer İstasyonu")
        self.initUI()
    def initUI(self):
        self.Serial_Port=QtWidgets.QLabel(self)
        self.Serial_Port.setGeometry(300,300,300,300)

        self.Baslat = QtWidgets.QPushButton(self)
        self.Baslat.setGeometry(100, 50, 100, 50)
        self.Baslat.setText("Başlat")

        self.Ayril = QtWidgets.QPushButton(self)
        self.Ayril.setGeometry(100, 100, 100, 50)
        self.Ayril.setText("Ayrıl")

        self.Motor_Ac = QtWidgets.QPushButton(self)
        self.Motor_Ac.setGeometry(100, 150, 100, 50)
        self.Motor_Ac.setText("Motorları Aç")

        self.Motor_Kapa = QtWidgets.QPushButton(self)
        self.Motor_Kapa.setGeometry(100, 200, 100, 50)
        self.Motor_Kapa.setText("Motorları Kapat")

        self.Video_Sec = QtWidgets.QPushButton(self)
        self.Video_Sec.setGeometry(250, 50, 100, 50)
        self.Video_Sec.setText("Video Seç")

        self.Video_Gonder = QtWidgets.QPushButton(self)
        self.Video_Gonder.setGeometry(250, 100, 100, 50)
        self.Video_Gonder.setText("Video Gönder")

        self.Kalibrasyon = QtWidgets.QPushButton(self)
        self.Kalibrasyon.setGeometry(250, 150, 100, 50)
        self.Kalibrasyon.setText("Kalibrasyon")

        self.Asenkron_Video = QtWidgets.QPushButton(self)
        self.Asenkron_Video.setGeometry(250, 200, 100, 50)
        self.Asenkron_Video.setText("Asenkron Video")

    def Update(self):
        self.Serial_Port.setText("Sicaklik Degeri "+str(ser.read_until(size=5)))

def window():
    app= QApplication(sys.argv)
    win= Window()
    win.show()
    win.Update()
    sys.exit(app.exec_())

ser = serial.Serial("COM5","9600")
window()