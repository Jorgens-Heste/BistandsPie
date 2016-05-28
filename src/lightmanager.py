import serial

import time
from requests.sessions import session


class LightManager(object):

    def __init__(self):
        try:
            port = "/dev/ttyACM4"
            self.ser = serial.Serial(port, 9600)
        except:
            print "NO LIGHT MANAGER ATTACHED"

    def __del__(self):
        self.ser.close()

    def setSession(self, sessionnumber):
        try:
            print "Sendign session number"
            x = self.ser.write(str(sessionnumber))
            time.sleep(0.0001)
            print x

        except:
            print "LIGHT MANAGER NOT ATTACHED PROPERLY"
