

@app.route('/newsomething/')
def getRefresh():
    res = False
    return jsonify(res = None)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('sessions.html', name=name)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
