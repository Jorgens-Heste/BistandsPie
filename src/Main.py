from flask import Flask, jsonify
from flask import render_template

from interaction import InteractionManager
from person import *
from reader import *
from conncections import FirebaseConnector


app = Flask(__name__)

#reader = MagReader()
reader = FakeReader("2343233")
connectionmanager = FirebaseConnector()

interactionManager = InteractionManager()
currentUser = ""

def initiateSession():
    currentuser = reader.readDataFromCardAndReturnPerson()

    sessionnumber = connectionmanager.lookupUserSessionNumber(currentuser)

    interactionManager.setUser(currentuser)
    interactionManager.sendUserToSession(sessionnumber)

    connectionmanager.incrementSession(currentuser)



@app.route('/')
def hello_world():
    initiateSession()
    return interactionManager.getContent()

if __name__ == '__main__':
    app.run()






