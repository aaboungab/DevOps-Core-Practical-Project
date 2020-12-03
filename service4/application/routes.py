from flask import Flask, Response, request
import random
from application import app

@app.route('/name', methods=['GET','POST'])
def name():

    info = request.data.decode('utf-8')
    data = info.split(" ")
    position = data[0]
    team = data[1]

    if team == "Arsenal":
        if position == 'Striker':
            name = 'Pierre-Emerick Aubameyang'
        elif position == 'Midfield':
            name = 'Mesut Ozil'
        elif position == 'CenterBack':
            name = 'Gabriel Magalhaes'
    elif team == "Chelsea":
        if position == 'Striker':
            name = 'Olivier Giroud'
        elif position == 'Midfield':
            name = 'Mateo Kovacic'
        elif position == 'CenterBack':
            name = 'Kurt Zouma'
    elif team == "Liverpool":
        if position == 'Striker':
            name = 'Mohamed Salah'
        elif position == 'Midfield':
            name = 'Georginio Wijnaldum'
        elif position == 'CenterBack':
            name = 'Virgil van Dijk'
    else:
        return "player not found"

    
    return Response(name, mimetype="text/plain")