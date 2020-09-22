from flask import flask
app = flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello python!'

if __name__ == '__main__':
    app.run()