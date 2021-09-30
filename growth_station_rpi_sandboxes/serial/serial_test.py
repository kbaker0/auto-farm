import serial

ser = serial.Serial('/dev/ttyACM0')
print(ser.name)
ser.write(b'0')
ser.flush()
incoming = ser.readline()
print(incoming)
ser.close()
