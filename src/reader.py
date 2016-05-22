from person import *
import time
import serial

class MagReader(object):


    def __init__(self):
        self.currentPerson = Person()



    def readDataFromCardAndReturnPerson(self):


        data = self.readData();
        resperson = self.parseData(data)


        #Reads card gets data and some number
        return self.currentPerson


    def readData(self):
        data = False
        while not data:

            with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
                # x = ser.read()          # read one byte
                ##s = ser.read(10)        # read up to ten bytes (timeout)
                line = ser.readline()   # read a '\n' terminated line
                print line

                if line != "":
                    data = True
        return line

    def parseData(self, data):
        self.parseTrack2(data)

    def parseTrack2(self, data):
        self.parseCPR(data)
        self.parseName(data)
        self.parseCity(data)

    def parseCPR(self, data):
        cpr = data[8:18]
        self.currentPerson.setCPR(cpr)

    def parseName(self, data):
        name = data[8:18]
        self.currentPerson.setName(name)


    def parseCity(self, data):
        bycode = data[28:31] #Looks op city from dictionary below
        by = self.cities[bycode]
        self.currentPerson.setCity(by)



    cities = {
        '101': 'Koebenhavn',
        '147': 'Frederiksberg',
        '151': 'Ballerup',
        '153': 'Broendby',
        '155': 'Dragoer',
        '157': 'Gentofte',
        '159': 'Gladsaxe',
        '161': 'Glostrup',
        '163': 'Herlev',
        '165': 'Albertslund',
        '167': 'Hvidovre',
        '169': 'Hoeje-Taastrup',
        '173': 'Lyngby-Taarbaek',
        '175': 'Roedovre',
        '183': 'Ishoej',
        '185': 'Taarnby',
        '187': 'Vallensbaek',
        '190': 'Furesoe',
        '201': 'Alleroed',
        '210': 'Fredensborg',
        '217': 'Helsingoer',
        '219': 'Hilleroed',
        '223': 'Hoersholm',
        '230': 'Rudersdal',
        '240': 'Egedal',
        '250': 'Frederikssund',
        '260': 'Frederiksvaerk-Hundested',
        '270': 'Gribskov',
        '400': 'Bornholm',
        '253': 'Greve',
        '259': 'Koege',
        '265': 'Roskilde',
        '269': 'Solroed',
        '306': 'Odsherred',
        '316': 'Holbaek',
        '320': 'Faxe',
        '326': 'Kalundborg',
        '329': 'Ringsted',
        '330': 'Slagelse',
        '336': 'Stevns',
        '340': 'Soroe',
        '350': 'Lejre',
        '360': 'Lolland',
        '370': 'Naestved',
        '376': 'Guldborgsund',
        '390': 'Vordingborg',
        '410': 'Middelfart',
        '420': 'Assens',
        '430': 'Faaborg-Midtfyn',
        '440': 'Kerteminde',
        '450': 'Nyborg',
        '461': 'Odense',
        '479': 'Svendborg',
        '480': 'Bogense',
        '482': 'Langeland',
        '492': 'aeroe',
        '510': 'Haderslev',
        '530': 'Billund',
        '540': 'Soenderborg',
        '550': 'Toender',
        '561': 'Esbjerg',
        '563': 'Fanoe',
        '573': 'Varde',
        '575': 'Vejen',
        '580': 'Aabenraa',
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
        '741': 'Samsoe',
        '746': 'Skanderborg',
        '751': 'Aarhus',
        '756': 'Ikast--Brande',
        '760': 'Ringkoebing-Skjern',
        '779': 'Skive',
        '791': 'Viborg',
        '773': 'Morsoe',
        '787': 'Thisted',
        '810': 'Broenderslev-Dronninglund',
        '813': 'Frederikshavn',
        '820': 'Vesthimmerland',
        '825': 'Laesoe',
        '840': 'Rebild',
        '846': 'Mariagerfjord',
        '849': 'Jammerbugt',
        '851': 'Aalborg',
        '860': 'Hjoerring'}

