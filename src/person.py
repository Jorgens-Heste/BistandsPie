class Person(object):

    def setCPR(self, cpr):
        self.cpr = cpr
        date = cpr[0 : (len(cpr) - 4)]
        self.birthday = date[0:2] + "/" + date[2:4] + "/" + date[4:6]
        self.age = 2016 - int("19" + date[4:6])
        print self.name + " er " + str(self.age) + " gammel"

    def setName(self, name):
        self.name = name

    def setLastName(self, lastname):
        self.lastName = lastname

    def setCity(self, city):
        self.city = city

    def setSession(self, session):
        self.session = session

    def setID(self, id):
        self.id = id

    def setAddress(self, address):
        self.address = address

    def setPostalcode(self, postalcode):
        self.postalCode = postalcode
