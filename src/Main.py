from person import *
from reader import *
from conncections import FirebaseConnector



#reader = MagReader()
reader = FakeReader("332332")
connectionmanager = FirebaseConnector()


while True:
    currentuser = reader.readDataFromCardAndReturnPerson()

    #connectionmanager.addUser(currentuser)

    #connectionmanager.addUser(currentuser)


    sessionnumber = connectionmanager.lookupUserSessionNumber(currentuser)
    print sessionnumber

    connectionmanager.incrementSession(currentuser)

    '''
    if status:
        print "ARH troar wi har set ham foer"
    else:
        print "ARH tror ikk wi har set hem foear"
    '''



    break




    #print(currentuser.name)
    #print(currentuser.city)
    #print(currentuser.cpr)






