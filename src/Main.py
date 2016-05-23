from person import *
from reader import *
from conncections import FirebaseConnector



#reader = MagReader()
reader = FakeReader()
connectionmanager = FirebaseConnector()


while True:
    currentuser = reader.readDataFromCardAndReturnPerson()

    connectionmanager.getUsers()
    connectionmanager.lookupUser()

    break




    #print(currentuser.name)
    #print(currentuser.city)
    #print(currentuser.cpr)






