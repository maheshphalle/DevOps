from flask import Flask, request, jsonify

#createing s server

app = Flask(__name__)

@app.route('/')

def hello_world():

    return 'Hello, World!'

if __name__ == '__main__':

    app.run(debug=True)