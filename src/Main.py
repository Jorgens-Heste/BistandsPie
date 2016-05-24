import threading

from flask import Flask, jsonify
from flask import render_template

from interaction import InteractionManager
from matte import MatteReader
from person import *
from reader import *
from conncections import FirebaseConnector


app = Flask(__name__)

reader = MagReader()
#reader = FakeReader("264846") # For testing
connectionmanager = FirebaseConnector()
matte = MatteReader()

interactionManager = InteractionManager()
currentUser = ""

def initiateSession():
    currentuser = reader.readDataFromCardAndReturnPerson()

    sessionnumber = connectionmanager.lookupUserSessionNumber(currentuser)

    interactionManager.setUser(currentuser)
    interactionManager.sendusertosession(sessionnumber)

    connectionmanager.incrementSession(currentuser)

def worker():
    matte.checkMatte()

thread = threading.Thread(target=worker)

@app.before_first_request
def startMatteReadingLoop():
    thread.start()

@app.route('/')
def startinteraction():
    initiateSession()
    session = interactionManager.getContent()
    matte.reset()

    return render_template('sessions.html', session = session)

@app.route('/matte-status/')
def matteStatus():
    return matte.alive


if __name__ == '__main__':
    app.debug = True
    app.run()






