import time


class MatteReader(object):

    def __init__(self):
        self.alive = "1"

    def checkMatte(self):

        #Simulkate waiting while loope with sleep
        time.sleep(10)
        self.alive = "0"


    def getStatus(self):
        return self.alive

