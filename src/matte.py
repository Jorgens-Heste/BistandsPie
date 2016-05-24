import time


class MatteReader(object):

    alive = True

    def checkMatte(self):

        #Simulkate waiting while loope with sleep
        time.sleep(10)
        self.alive = False


    def getStatus(self):
        return self.alive

