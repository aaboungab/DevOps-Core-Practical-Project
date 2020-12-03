from flask import Flask, Response, request
import random
from application import app

@app.route('/position', methods=['GET'])
def position():
    
    positions = ["Striker", "Midfield", "CenterBack"]
    position = positions[random.randrange(0,3)]

    return Response(position, mimetype="text/plain")