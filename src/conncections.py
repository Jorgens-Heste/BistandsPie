from random import randint

from firebase import *

class FirebaseConnector(object):

    def __init__(self):
        self.firebase = firebase.FirebaseApplication('https://bistandsserver.firebaseio.com', None)

    def getUsers(self):
        result = self.firebase.get('/users', None)
        return result

    def lookupUserSessionNumber(self, person):
        user = self.findUser(person)

        if user != "":
            print "WI KENDER DIG"
            sessionnumber =  self.lookupUserSession(user)
            person.setSession(sessionnumber) # LOOK HERE: Possible source of problems  This should be done in a more clever way I just can not think of one right now
            return sessionnumber
        else:
            self.addUser(person)
            self.findAndUpdateFirebaseID(person)
            print "WI KENDER DIG IKK"

            return 0


    """
    Increments the session attribute of a user on forebase backend
    Requires that the find object has been called on the user.So the id has been updated
    """
    def incrementSession(self, person):

        person.setSession(person.session + 1) # increment iD
        self.updateUser(person) # update the user so it fits the new data



    """
    Updates the users data so it matches the object given
    Requires that the find object has been called on the user.So the id has been updated
    """
    def updateUser(self, person):


        userbody = self.generateUserData(person)

        data = {person.id : userbody}

        self.makePatchCall(data)


    """
    Returns the body of a json user matching the data in the object given
    """
    def generateUserData(self, person):

        return { "firstname": person.name, "lastname": person.lastName,  "cpr": person.cpr,  "address": person.address, "city": person.city,  "money": person.money, "postalcode": person.postalCode,   "session": person.session }


    """
    Change the user object depending onthe data
    Requires that the find object has been called on the user.So the id has been updated
    """

    def makePatchCall(self, data):
        #self.firebase.put('/users', data = { "name": "DATA HAHA"} , params={'print': 'pretty'})
        result = self.firebase.patch('/users/', data)




    def addUser(self, person):
        #result2 = self.firebase.put('/ users', data = {"238329": {"name": "mr mr"}})

        person.setSession(0)
        person.setMoney(randint(5000, 20000))
        data = self.generateUserData(person)
        result = self.firebase.post('/users', data , params={'print': 'pretty'})
        print result


    def findAndUpdateFirebaseID(self, person):
        users = self.getUsers()

        try:
            for id in users:
                userbody = users.get(id) # get a reference to userbody from  firebase user ID
                usercpr = self.lookUpUserCPR(userbody)

                if usercpr == person.cpr:
                    person.setID(id) # LOOK HERE: Possible source of problems  This should be done in a more clever way I just can not think of one right now

        except TypeError: # if no user has been added we ignore this and asume that we dont know anybody
            pass





    #Given er person object returns a json representation on the body of the object
    #also records the CPR of the person object
    def findUser(self, person):
        users = self.getUsers()

        try:
            for id in users:
                userbody = users.get(id) # get a reference to userbody from  firebase user ID
                usercpr = self.lookUpUserCPR(userbody)

                if usercpr == person.cpr:
                    person.setID(id) # LOOK HERE: Possible source of problems  This should be done in a more clever way I just can not think of one right now
                    person.setMoney(userbody.get("money"))
                    return userbody

        except TypeError: # if no user has been added we ignore this and asume that we dont know anybody
            pass

        return ""

    def lookupUserSession(self, userbody):
        return userbody.get("session")

    def lookUpUserCPR(self, userbody):
        return userbody.get("cpr")












