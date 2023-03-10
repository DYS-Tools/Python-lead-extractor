from flask import Flask, jsonify

from controllers.dorking import DorkingController

app = Flask(__name__)

@app.route('/')


def index():
    return "Bienvenue sur notre API ! "

@app.route('/api/<dorking>')
def requestDorking(dorking):
    return DorkingController().request(dorking)

if __name__ == "__main__":
    app.run()
