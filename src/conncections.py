from firebase import *
import json

class FirebaseConnector(object):

    def __init__(self):
        self.firebase = firebase.FirebaseApplication('https://bistandsserver.firebaseio.com', None)


    def getUsers(self):
        result = self.firebase.get('/users', None)
        return result

    def lookupUser(self):
        users = self.getUsers()

        for id in users:
            print id

        print users




