from person import *
import time
import serial

class MagReader(object):


    def __init__(self):
        self.currentPerson = Person


    def readDataFromCardAndReturnPerson(self):


        data = self.readData();
        resperson = self.parseData(data)


        #Reads card gets data and some number
        return self.currentPerson


    def readData(self):
        data = False
        while not data:

            with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
                # x = ser.read()          # read one byte
                ##s = ser.read(10)        # read up to ten bytes (timeout)
                line = ser.readline()   # read a '\n' terminated line
                print line

                if line != "":
                    data = True
        return line

    def parseData(self, data):
        self.parseTrack2(data)

    def parseTrack2(self, data):

        print "CPR" + data[8:18]

        self.currentPerson.setCPR("d")


        
        



