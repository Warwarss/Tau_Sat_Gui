import serial
ser = serial.Serial("COM5","9600")  # open serial port
while (1):
    print(ser.read_until(size=5))         # check which port was really used
ser.close()             # close port