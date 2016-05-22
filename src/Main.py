from person import *
from reader import MagReader

reader = MagReader()

currentuser = reader.readDataFromCardAndReturnPerson()

print(currentuser.name)




