from flask import Flask, jsonify
from flask import render_template

from person import *
from reader import *
from conncections import FirebaseConnector


app = Flask(__name__)

#reader = MagReader()
reader = FakeReader("332332")
connectionmanager = FirebaseConnector()


while True:
    currentuser = reader.readDataFromCardAndReturnPerson()

    sessionnumber = connectionmanager.lookupUserSessionNumber(currentuser)
    print sessionnumber

    connectionmanager.incrementSession(currentuser)



    break

if __name__ == '__main__':
    app.run()






