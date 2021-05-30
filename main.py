from flask import Flask, render_template, request, session, redirect, jsonify
from flask_cors import CORS, cross_origin
from threading import Thread

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = "this_is_a_secret"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/program')
def program():
    return render_template('program.html')

@app.route('/program/<program_id>')
def program_search(program_id:int):
    return render_template('search.html', program_id=program_id)

@app.route('/err')
def err():
    return render_template('programe.html')

@app.route('/saves')
def saves():
    return render_template('saves.html')

def run():
    app.run(host = '0.0.0.0', port=8000)

def start():
    server = Thread(target = run)
    server.start()

start()