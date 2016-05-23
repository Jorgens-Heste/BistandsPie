from firebase import *
import json

class FirebaseConnector(object):

    def __init__(self):
        self.firebase = firebase.FirebaseApplication('https://bistandsserver.firebaseio.com', None)


    def getUsers(self):
        result = self.firebase.get('/users', None)
        return result

    def lookupUser(self, id):
        users = self.getUsers()

        for userid in users:
            if userid == id:
                return True

        return False

    def addUser(self, person):


        #result2 = self.firebase.put('/users', data = {"238329": {"name": "mr mr"}})

        result = self.firebase.post('/users', data = { "name": "Kapsper Heiselberg", "cpr": "363738372994", "by": "Aarhus" } , params={'print': 'pretty'})
        result = self.firebase.post('/users', data =  { "name": "Daniel Graungaard", "cpr": "0565872234", "by": "Aarhus" }, params={'print': 'pretty'})
        print result







