from flask import Flask, Response, request
import random
from application import app

@app.route('/team', methods=['GET'])
def team():

    teams = ["Arsenal", "Chelsea", "Liverpool"]

    team = teams[random.randrange(0,3)]
    
    return Response(team, mimetype="text/plain")