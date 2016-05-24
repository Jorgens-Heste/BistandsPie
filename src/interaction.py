# coding=utf-8
from random import randint
class Session(object):

    def __init__(self):
        self.sessionNumber = "0"
        self.elements = []
        self.heading = "Velkommen"


    def setSessionNumber(self, number):
        self.sessionNumber = number

    def setUser(self, user):
        self.user = user

    def appendElement(self, cssclass, content):

        unicode = content.decode('utf-8') # Convert utf 8 to unicode so blrowser can render it
        item = (cssclass, unicode)
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
        user = self.session.user

        self.session.appendElement("hilsen", "Hej " + user.name)

        for question in self.buildquestionList1():
            self.session.appendElement("question", question)

        self.session.appendElement("green", "Nuværende Addresse: " + user.address + ", " + user.city)



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

    def buildquestionList1(self):
        res = []

        max = len(self.questionsforone)
        print max
        for number in range(0, 5):
            choice = randint(0, max - 1)
            question = self.questionsforone[choice]
            res.append(question)

        return res




    questionsforone =  [
        "Har jeg råd til mad?",
        "Har jeg det jeg skal bruge i min hverdag?",
        "Hvordan har familien det?",
        "Er der sket noget jeg har behov for en anden til at snakke med om?",
        "Går det godt, alt taget i betragtning?",
        "Er de gamle skavanker helet?",
        "Hvornår har jeg sidst være ved lægen?",
        "Kunne jeg tænke mig at blive selvstændig?",
        "Var jeg glad for dit gamle arbejde?",
        "Lyst til at arbejde i en ny branche?",
        "Er jeg færdig med at uddanne mig?",
        "Hvad kan jeg blive?",
        "Hvor mange penge skal der til, for at jeg kan få det til at køre rundt?",
        "Er der balance i min økonomi?",
        "Er der mere jeg vil vide?"]
