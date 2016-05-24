import serial
import time


class MatteReader(object):

    def __init__(self):
        self.alive = "1"

    def checkMatte(self):

        while(True) :
            #Simulkate waiting while loope with sleep
            message = self.readData()

            if(message == "dead"):
                self.alive = "0"
            else:
                self.alive = "1"

            time.sleep(0.1)

    def getStatus(self):
        return self.alive

    def reset(self):
        self.alive = "1"


    def readData(self):
             data = False
             while not data:

                 with serial.Serial('/dev/ttyACM3', 9600, timeout=1) as ser:
                     # x = ser.read()          # read one byte
                     ##s = ser.read(10)        # read up to ten bytes (timeout)
                     line = ser.readline()   # read a '\n' terminated line
                     print "mat MESSAGE: "  + line

                     if line != "":
                         data = True
             return line