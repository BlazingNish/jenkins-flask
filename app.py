from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/message')
def message():
    return 'This is a message.'

if __name__ == '__main__':
    app.run(debug=True, port = 5000)