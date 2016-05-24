from reader import MagReader

magreader = MagReader()

user = magreader.readDataFromCardAndReturnPerson()

print user.name
print user.sirname
