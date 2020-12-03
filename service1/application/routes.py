from flask import Flask, render_template, request
import requests
from application import app


@app.route('/', methods=['GET','POST'])
def index():

    #get position
    position = requests.get("http://service2:5001/position")
    #get team name
    team = requests.get("http://service3:5002/team")
    #post player
    info = str(position.text) + " " + str(team.text)
    name = requests.post("http://service4:5003/name", data=info)

    return render_template('index.html', title='player team', position=position.text, team=team.text, info=info, name=name.text)