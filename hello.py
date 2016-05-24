from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('sessions.html', name=name)
