#!/usr/bin/env python3
from random import randrange
from flask import Flask, jsonify, render_template
import sys

class Sanasto:
    def __init__(itse, tiedosto):
        itse.sanat = []
        with open(tiedosto, mode="r", encoding="utf-8") as f:
            for rivi in f:
                pari = rivi.strip('\n').split('\t')
                if len(pari) == 2:
                    itse.sanat.append(pari)
                else:
                    print('Virhe:', pari)

    def arvo(itse):
        n = randrange(1, len(itse.sanat))
        return itse.sanat[n]

    def kielet(itse):
        return itse.sanat[0]

if len(sys.argv) == 2:
    tiedosto = sys.argv[1]
else:
    tiedosto = input('Anna tiedostonimi: ')
if tiedosto == '':
    tiedosto = 'sanat.txt'
sanasto = Sanasto(tiedosto)
    
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    kielet = sanasto.kielet()
    return render_template('index.html', kieli1=kielet[0], kieli2=kielet[1])

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route('/api/sanapari', methods=['GET'])
def api_sanapari():
    return jsonify(sanasto.arvo())

@app.route('/api/kielet', methods=['GET'])
def api_kielet():
    return jsonify(sanasto.kielet())

app.run(host='0.0.0.0', port=80)
