import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtSvg
from PyQt5.QtCore import QTimer
from qfi import qfi_ADI, qfi_ALT, qfi_SI, qfi_HSI, qfi_VSI, qfi_TC
from PyQt5.QtCore import QTimer
i = 0


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setWindowTitle("Stm Real Time Simulator")

        self.mainLayout = QVBoxLayout()
        self.upLayout = QFormLayout()
        self.layout = QGridLayout()

        self.mainLayout.addLayout(self.upLayout, 30)
        self.mainLayout.addLayout(self.layout, 70)
        self.pitch = QLabel("Pitch :  ")
        self.pitch_value = QLabel("...")
        self.pitch.setStyleSheet("color:red;")
        self.pitch_value.setStyleSheet("color:red;")
        self.roll = QLabel("Roll :  ")
        self.roll_value = QLabel("...")
        self.roll.setStyleSheet("color:green;")
        self.roll_value.setStyleSheet("color:green;")
        self.btn_connect = QPushButton("Enter", self)
        self.btn_exit = QPushButton("Exit", self)
        self.upLayout.addRow(self.pitch, self.pitch_value)
        self.upLayout.addRow(self.roll, self.roll_value)

        self.adi = qfi_ADI.qfi_ADI(self)
        self.adi.resize(300, 300)
        self.adi.reinit()
        self.layout.addWidget(self.adi, 0, 0)

        self.setLayout(self.mainLayout)

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update1)
        self.show()
        self.adi.setRoll(float(data[1]))

    def update1(self):
        global i
        line = str(self.ser.readline())
        print(line)
        data = line.split(",")
        print(data)
        self.pitch_value.setText(str(data[1]))
        self.roll_value.setText(str(data[2]))
        self.adi.setRoll(float(data[1]))
        self.adi.setPitch(float(data[2]))
        self.adi.viewUpdate.emit()

    def exit(self):
        self.timer.stop()
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())