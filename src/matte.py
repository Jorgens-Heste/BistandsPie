import time


class MatteReader(object):

    def __init__(self):
        self.alive = "1"

    def checkMatte(self):

        while(True) :
            #Simulkate waiting while loope with sleep
            time.sleep(30)
            self.alive = "0"


    def getStatus(self):
        return self.alive

    def reset(self):
        self.alive = "1"
