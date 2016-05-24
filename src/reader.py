# coding=utf-8
from debian.debtags import readTagDatabase
import re
from nis import match

from person import *
import time
import serial

class MagReader(object):


    def __init__(self):
        self.currentPerson = Person()



    def readDataFromCardAndReturnPerson(self):
        try:
            data = self.readData();
            self.parseData(data)
        except ValueError: #Try again if error
            print "VALUE ERROR"
            self.readDataFromCardAndReturnPerson()


        #Reads card gets data and some number
        return self.currentPerson



    def readData(self):
        print "Swipe card"
        data = raw_input()
        return data

    def parseData(self, data):

        #track1
        self.parseName(data)
        #track2
        self.parseAddress(data)
        self.parseCity(data)
        self.parseZipCode(data)
        self.parseCPR(data)


    def parseAddress(self, data):
        withoutfront = data[35 : len(data) - 1]

        #Find end
        regexpattern = re.compile("\s\s\s")
        match = regexpattern.search(withoutfront)
        spaceendindex = match.end()

        rawaddress = withoutfront[0:spaceendindex]

        rawaddress = self.replaceDanishLetters(rawaddress)

        adressparts = rawaddress.split(" ")

        result = ""
        for word in adressparts:
            result = result + " " + self.utf8Title(word)

        result = result[1: len(result)] # Remove first space

        result  = result.replace("-", "v. ") #Prettify room numbers

        self.currentPerson.setAddress(result)

    def parseCPR(self, data):
        cpr = data[86:96]
        self.currentPerson.setCPR(cpr)

    def parseName(self, data):
        rawname = data[1:25]

        splitter = rawname.index('^')


        forname = rawname[splitter + 1 :len(rawname)]
        sirname = rawname[0:splitter]

        forname = self.replaceDanishLetters(forname)
        sirname = self.replaceDanishLetters(sirname)

        forname = self.utf8Title(forname)
        sirname = self.utf8Title(sirname)

        self.currentPerson.setName(forname)
        self.currentPerson.setLastName(sirname)



    def parseCity(self, data):
        bycode = data[69:72] #Looks op city from dictionary below
        by = self.cities[bycode]
        self.currentPerson.setCity(by)

    def parseZipCode(self, data):
        postalcode = data[72:76] #Looks op city from dictionary below
        self.currentPerson.setPostalcode(postalcode)





    cities = {
        '101': 'København',
        '147': 'Frederiksberg',
        '151': 'Ballerup',
        '153': 'Brøndby',
        '155': 'Dragør',
        '157': 'Gentofte',
        '159': 'Gladsaxe',
        '161': 'Glostrup',
        '163': 'Herlev',
        '165': 'Albertslund',
        '167': 'Hvidovre',
        '169': 'Høje-Tåstrup',
        '173': 'Lyngby-Tårbæk',
        '175': 'Rødovre',
        '183': 'Ishøj',
        '185': 'Tårnby',
        '187': 'Vallensbæk',
        '190': 'Furesø',
        '201': 'Allerød',
        '210': 'Fredensborg',
        '217': 'Helsingør',
        '219': 'Hillerød',
        '223': 'Hørsholm',
        '230': 'Rudersdal',
        '240': 'Egedal',
        '250': 'Frederikssund',
        '260': 'Frederiksværk-Hundested',
        '270': 'Gribskov',
        '400': 'Bornholm',
        '253': 'Greve',
        '259': 'Køge',
        '265': 'Roskilde',
        '269': 'Solrød',
        '306': 'Odsherred',
        '316': 'Holbæk',
        '320': 'Faxe',
        '326': 'Kalundborg',
        '329': 'Ringsted',
        '330': 'Slagelse',
        '336': 'Stevns',
        '340': 'Sorø',
        '350': 'Lejre',
        '360': 'Lolland',
        '370': 'Næstved',
        '376': 'Guldborgsund',
        '390': 'Vordingborg',
        '410': 'Middelfart',
        '420': 'Assens',
        '430': 'Fåborg-Midtfyn',
        '440': 'Kerteminde',
        '450': 'Nyborg',
        '461': 'Odense',
        '479': 'Svendborg',
        '480': 'Bogense',
        '482': 'Langeland',
        '492': 'Ærø',
        '510': 'Haderslev',
        '530': 'Billund',
        '540': 'Sønderborg',
        '550': 'Tønder',
        '561': 'Esbjerg',
        '563': 'Fanø',
        '573': 'Varde',
        '575': 'Vejen',
        '580': 'åbenrå',
        '607': 'Fredericia',
        '621': 'Kolding',
        '630': 'Vejle',
        '615': 'Horsens',
        '657': 'Herning',
        '661': 'Holstebro',
        '665': 'Lemvig',
        '671': 'Struer',
        '706': 'Syddjurs',
        '707': 'Norddjurs',
        '710': 'Favrskov',
        '727': 'Odder',
        '730': 'Randers',
        '766': 'Hedensted',
        '740': 'Silkeborg',
        '741': 'Samsø',
        '746': 'Skanderborg',
        '751': 'Århus',
        '756': 'Ikast--Brande',
        '760': 'Ringkøbing-Skjern',
        '779': 'Skive',
        '791': 'Viborg',
        '773': 'Morsø',
        '787': 'Thisted',
        '810': 'Brønderslev-Dronninglund',
        '813': 'Frederikshavn',
        '820': 'Vesthimmerland',
        '825': 'Læsø',
        '840': 'Rebild',
        '846': 'Mariagerfjord',
        '849': 'Jammerbugt',
        '851': 'Aalborg',
        '860': 'Hjørring'}



    def replaceDanishLetters(self, string):
        string = string.replace("\\", "Ø")
        string = string.replace("[", "Æ")
        string = string.replace("]", "Å")

        return string

    def utf8Title(self, string):
        string = string.decode('utf8').title()
        string = string.encode('utf8')
        return string



#For eayly testing
#yes this should probably not live here but it is easier to do testing and this is a prototype and miles way from production anyway
class FakeReader(object):

    def __init__(self, cpr):
        self.cpr = cpr

    def readDataFromCardAndReturnPerson(self):

        result = Person()

        result.setName("Daniel")
        result.setLastName("Graungaard")
        result.setCity("Aarhus")
        result.setAddress("Engdalgårdsvej 156 st tv v 1")
        result.setCity("Aarhus")
        result.setPostalcode("8330")
        result.setCPR(self.cpr)


        time.sleep(2)
        return result