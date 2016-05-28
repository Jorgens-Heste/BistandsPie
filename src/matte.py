import serial
import time


class MatteReader(object):

    def __init__(self):
        self.alive = "1"

    def checkMatte(self):

        while(True) :
            #Simulkate waiting while loope with sleep
            message = self.readData()

            if(message == "D"):
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
                     character = ser.read()          # read one byte
                     ##s = ser.read(10)        # read up to ten bytes (timeout)
                     #line = ser.readline()   # read a '\n' terminated line

                     if character != "":
                         data = True
             return character



class FakeMatteReader(object):

    def __init__(self, delay):
        self.alive = "1"
        self.delay = delay

    def checkMatte(self):

        while(True) :
            #Simulkate waiting while loope with sleep
            time.sleep(self.delay)
            self.alive = "0"


    def getStatus(self):
        return self.alive

    def reset(self):
        self.alive = "1"
