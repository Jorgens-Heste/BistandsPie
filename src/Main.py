from flask import Flask, jsonify
from flask import render_template

from interaction import InteractionManager
from person import *
from reader import *
from conncections import FirebaseConnector


app = Flask(__name__)

#reader = MagReader()
reader = FakeReader("23343433")
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
def startinteraction():
    initiateSession()
    session = interactionManager.getContent()

    return render_template('sessions.html', session = session)


if __name__ == '__main__':
    app.run()






