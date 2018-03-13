import time
import serial #Comms for the arduino

ser = serial.Serial('/dev/ttyACM0', 9600)
ser_confirmation = 0
print('Starting up Comms\n')
time.sleep(2)
print('Running wave demo\n')
ser_byte = '0'
ser_byte2 = '0'

def main():
    while 1:
        ser_byte = '10000000'
        ser_byte2 = '00000000'
        sendData(ser_byte, ser_byte2)
        ser_byte = '01000000'
        ser_byte2 = '00000000'
        sendData(ser_byte, ser_byte2)
        ser_byte = '00000000'
        ser_byte2 = '10000000'
        sendData(ser_byte, ser_byte2)
        ser_byte = '00000000'
        ser_byte2 = '01000000'
        sendData(ser_byte, ser_byte2)
        ser_byte = '00010000'
        ser_byte2 = '00000000'
        sendData(ser_byte, ser_byte2)
        ser_byte = '00100000'
        ser_byte2 = '00000000'
        sendData(ser_byte, ser_byte2)

def sendData(ser_byte, ser_byte2):
        # Send First byte
        ser.write(chr(int(ser_byte, 2)))
        print('1st Character Value: ' + chr(int(ser_byte, 2)) + "\n")
        print('1st Binary Value: ' + ser_byte + '\n')

        # Send Second byte
        ser.write(chr(int(ser_byte2, 2)))
        print('2nd Character Value: ' + chr(int(ser_byte2, 2)) + "\n")
        print('2nd Binary Value: ' + ser_byte2 + "\n")

        ser_confirmation = ser.read()

        # Make sure the arduino has time to process everything
        while ser_confirmation != chr(int(ser_byte, 2)):
            print("Value received from arduino: " + ser_confirmation)
            ser_confirmation == ser.read()
            time.sleep(.5)

# call main
if __name__ == '__main__':
    main()
