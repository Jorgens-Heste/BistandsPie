from reader import MagReader

magreader = MagReader()

user = magreader.readDataFromCardAndReturnPerson()

print user.city
print user.name
print user.lastName
print user.postalcode
print user.address
print user.cpr
