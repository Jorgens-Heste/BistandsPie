from flask import Flask, jsonify
from flask import render_template

from interaction import InteractionManager
from matte import MatteReader
from person import *
from reader import *
from conncections import FirebaseConnector


app = Flask(__name__)

#reader = MagReader()
reader = FakeReader("23343433")
connectionmanager = FirebaseConnector()
matte = MatteReader()

interactionManager = InteractionManager()
currentUser = ""

def initiateSession():
    currentuser = reader.readDataFromCardAndReturnPerson()

    sessionnumber = connectionmanager.lookupUserSessionNumber(currentuser)

    interactionManager.setUser(currentuser)
    interactionManager.sendUserToSession(sessionnumber)

    connectionmanager.incrementSession(currentuser)

def run():
    matte.checkMatte()

@app.route('/')
def startinteraction():
    initiateSession()
    session = interactionManager.getContent()

    return render_template('sessions.html', session = session)

@app.route('matte-status')
def matteStatus():
    return jsonify(matte.alive)


if __name__ == '__main__':
    app.run()






