from firebase import *
import json



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
            return self.lookupUserSession(user)
        else:
            self.addUser(person)
            print "WI KENDER DIG IKK"

            return 0


    def addUser(self, person):


        #result2 = self.firebase.put('/ users', data = {"238329": {"name": "mr mr"}})

        result = self.firebase.post('/users', data = { "name": person.name, "cpr": person.cpr, "by": person.city, "session": 0} , params={'print': 'pretty'})
        print result

    def findUser(self, person):
        users = self.getUsers()

        for id in users:
            userbody = users.get(id) # get a reference to userbody from  firebase user ID
            usercpr = self.lookUpUserCPR(userbody)

            if usercpr == person.cpr:
                return userbody

        return ""

    def lookupUserSession(self, userbody):
        return userbody.get("session")

    def lookUpUserCPR(self, userbody):
        return userbody.get("cpr")












