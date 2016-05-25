# coding=utf-8
from random import randint
import random

from datepicker import DatePicker
from lightmanager import LightManager


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
        unicode = content.decode('utf-8')  # Convert utf 8 to unicode so blrowser can render it
        item = (cssclass, unicode)
        self.elements.append(item)

    def setHeading(self, heading):
        self.heading = heading



class InteractionManager(object):
    datePicker = DatePicker()
    session = Session()
    lightmanager = LightManager()

    def setUser(self, user):
        self.user = user

    def sendusertosession(self, previoussession):

        self.session = Session()
        self.session.setUser(self.user)


        if previoussession == 0:
            self.startSession1()
        elif previoussession == 1:
            self.startSession2()
        else:
            self.startSession3()

        self.lightmanager.setSession(previoussession + 1) # Runs light in current phaase

    def startSession1(self):
        self.session.setSessionNumber("1")
        self.session.setHeading("Afklaring")

        user = self.session.user  # get the user from the session
        self.session.appendElement("hilsen", "Hej " + user.name)

        for question in self.buildList(self.questionsforone, 5):
            self.session.appendElement("question", question)

        for statement in self.buildList(self.economyStatements, 2):
            number = randint(5000, 20000)
            concatenate = statement % (number)
            print concatenate
            self.session.appendElement("blue", concatenate)

        self.session.appendElement("green", "Nuværende Addresse: " + user.address + ", " + user.city)
        for statement in self.buildList(self.workstatements, 2):
            self.session.appendElement("green", statement)

        self.session.appendElement("red", "Fødselsdato: " + user.birthday)
        date = self.datePicker.randomDate("1/1/2012", "24/5/2016", random.uniform(0, 1))
        print date
        self.session.appendElement("red", "Du var sidst ved lægen den: " + date)

        for statement in self.buildList(self.healthstatements, 1):
            self.session.appendElement("red", statement)

        print "Starter session: 1"

    def startSession2(self):
        self.session.setSessionNumber("2")
        self.session.setHeading("Valg")

        user = self.session.user  # get the user from the session
        self.session.appendElement("hilsen", "Velkommen tilbage " + user.name)

        self.session.appendElement("valg", self.makeChoice(user))

        self.session.appendElement("telefon",
                                   "Økonomisk rådgivning kan tilgås via kommunen på tlf: 41 85 63 86 mellem 09.00 og 14.00 på alle hverdage")

        print "Starter session: 2"

    def makeChoice(self, person):
        if person.age < 30:
            self.session.appendElement("udannelse", "En Uddannelsesvejleder kan snakke med omkring din fremtid på 33925000, alle hverdage fra 09.00 til 14.00.")
            return "Du har ikke ret til kontanthjælp, du kan i stedet for modtage uddannnelseshjælp."
        else:
            return self.choicelist[randint(0, len(self.choicelist) - 1)]

    def startSession3(self):
        self.session.setSessionNumber("3")
        self.session.setHeading("Fremtid")
        print "Starter session: 3"

    def getContent(self):
        return self.session

    """
    Precondition list should be bigger than max or endless recursion
    """

    def buildList(self, list, max):
        res = []
        numlist = []

        highest = len(list)
        print max

        for number in range(0, max):
            choice = self.guessnumber(0, highest - 1, numlist)
            statement = list[choice]
            res.append(statement)

        return res

    def guessnumber(self, min, max, list):
        num = randint(min, max)
        for number in list:
            if num == number:
                return self.guessnumber(min, max, list)

        list.append(num)

        return num

    questionsforone = [
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

    economyStatements = [

        "Der står %d på din konto",
        "Samlet set ejer du %d kroner",
        "Du har lån for %d kroner."]

    healthstatements = [
        "Din journal siger du døjer med rygproblemer.",
        "Du har været ved lægen sidste måned med ondt i knæet ved en sportskade.",
        "Din journal siger du har problemer i højre håndled fra arbejde ved din bærbare computer.",
        "Du mangler anden vaccination af din Hepapitis B for at fuldt ud vaccineret.",
        "Du har været ved vagtlægen 3 gange i løbet af sidste år."]

#forventer antal(d) er en integer imellem 1 og 6 år. og at klub(s) er en string fra listen volunteerclubs
    workstatements = [
        "Du betragtes som erfaren indenfor din branche.",
        "Du har været været ansat i %d år, i dit sidste job.",
        "Du har snart jubilæum i %s",
        "%s har haft dig som bestyrelsesmedlem i %d år",
        "Dine evner er eftertragtet hos erhvervslivet i øjeblikket.",
        "Du har en god chance for at komme hurtigt i nyt job."]

    volunteerclubs = [
        "fodboldkluben",
        "håndboldkluben",
        "klatreklubben",
        "golfklubben",
        "petanqueklubben",
        "dartklubben",
        "open space aarhus",
        "sportsklubben"]

    choicelist = [
        "Du har ikke ret til kontanthjælp, da du efter reglerne er i stand til at forsørge dig selv.",
        "Du har ikke ret til kontanthjælp, eftersom du har nok penge på dine konti til selvforsørgelse.",
        "Du har efter reglerne ret til kontanthjælp, da du er bedømt til ikke at være i stand til at forsørge dig selv på grund af helbredsmæssige årsager.",
        "På grund af dine økonomiske årsager er du blevet bedømt som havende krav på modtage kontanthjælp.",
        "Da du står uden forsørger efter samlivsophør, er du blevet berettiget kontanthjælp."]
