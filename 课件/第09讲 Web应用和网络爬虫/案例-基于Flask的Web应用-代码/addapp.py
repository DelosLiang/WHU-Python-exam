from flask import Flask, request
import flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/add', methods=['GET', 'POST'])
def add():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')
    else:
        n1 = int(request.form['n1'])
        n2 = int(request.form['n2'])
        s = n1 + n2
        return flask.render_template('result.html',n1=n1,n2=n2,n3=s)

if __name__ == '__main__':
    app.run()


