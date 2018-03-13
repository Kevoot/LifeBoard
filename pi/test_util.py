import serial
import time
import sys

ser = serial.Serial('/dev/ttyACM0', 9600)
print("initializing\n")
time.sleep(2)
ser.write(chr(int(sys.argv[1], 2)))
