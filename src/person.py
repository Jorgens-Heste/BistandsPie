class Person(object):

    def setCPR(self, cpr):
        self.cpr = cpr
        date = cpr[0 : (len(cpr) - 4)]
        self.birthday = date[0:2] + "/" + date[2:4] + "/" + date[4:6]

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
