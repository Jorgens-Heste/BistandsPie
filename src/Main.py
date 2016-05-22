from person import *
from reader import MagReader

reader = MagReader()

while True:
    currentuser = reader.readDataFromCardAndReturnPerson()


    print(currentuser.name)
    print(currentuser.city)
    print(currentuser.cpr)





