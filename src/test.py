from reader import MagReader

magreader = MagReader()

user = magreader.readDataFromCardAndReturnPerson()

print user.city
print user.name
print user.sirname
print user.postalcode
print user.address
print user.cpr
