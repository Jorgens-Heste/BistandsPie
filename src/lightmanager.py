import serial

import time
from requests.sessions import session


class LightManager(object):

    def __init__(self):
        port = "/dev/ttyACM5"
        self.ser = serial.Serial(port, 9600)

    def __del__(self):
        self.ser.close()

    def setSession(self, sessionnumber):
        print "Sendign session number"
        x = self.ser.write(str(sessionnumber))
        time.sleep(0.0001)
        print x
