

class InteractionManager(object):

    session = "0"

    def setUser(self, user):
        self.user = user


    def sendUserToSession(self, previoussession):

        if previoussession == 0:
            self.startSession1()
        elif previoussession == 1:
            self.startSession2()
        else:
            self.startSession3()


    def startSession1(self):
        self.session = "1"
        print "Starter session: 1"


    def startSession2(self):
        self.session = "2"
        print "Starter session: 2"


    def startSession3(self):
        self.session = "3"
        print "Starter session: 3"

    def getContent(self):
        return self.session




