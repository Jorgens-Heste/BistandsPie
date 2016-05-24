class Session(object):
    sessionNumber = "0"
    elements = ()
    heading = "velkommen"


    def setSessionNumber(self, number):
        self.sessionNumber = number

    def setUser(self, person):
        self.person = person

    def appendElement(self, cssclass, content):
        item = (cssclass, content)
        self.elements.append(item)

    def setHeading(self, heading):
        self.heading = heading



class InteractionManager(object):

    session = Session()

    def setUser(self, user):
        self.user = user

    def sendUserToSession(self, previoussession):

        self.session = Session()
        self.session.setUser(self.user)

        if previoussession == 0:
            self.startSession1()
        elif previoussession == 1:
            self.startSession2()
        else:
            self.startSession3()


    def startSession1(self):
        self.session.setSessionNumber("1")
        self.session.setHeading("Afklaring")

        print "Starter session: 1"


    def startSession2(self):
        self.session.setSessionNumber("2")
        self.session.setHeading("Valg")

        print "Starter session: 2"

    def startSession3(self):
        self.session.setSessionNumber("3")
        self.session.setHeading("Fremtid")
        print "Starter session: 3"

    def getContent(self):
        return self.session




