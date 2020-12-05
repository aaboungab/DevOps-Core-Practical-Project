# Week 9 Practical Project
# Football player generator

# Author
## Anas Aboungab

### Links
- Trello
- Risk Assessment
- Website 

## Contents
- [Brief](#brief)
    - [Objective](#obj)
    - [Requirements](#reqs)
    - [Project Approach](#approach)
- [Architecture](#arch)
    - [Entity Relationship Diagrams](#erd)
- [CI Pipeline](#ci)
- [Project Planning & User Stories](#use_case)
- [Testing](#test_)
- [Deployment](#depl)
- [Technologies used](#tech)
- [Risk Assessment](#risks)
    - [Explanation](#risk-exp)
- [Front end Design](#FE)
- [Successes](#suc)
- [Future Improvements](#improve)

### Prerequisites
- Git
- Docker
- Docker-compose

<a name="breif"></a>
## Breif

<a name="obj"></a>
### Objective
The objective of the DevOps Core Practical Project is to create an application that generates **objects** upon a set of predefined rules. 
The project must include the below core concepts which we have covered in training:
- Software Development with Python
Use of python modules that we have covered in the previous project (Flask, Jinja2, pymysql)
- Continuous Integration 
Use of Jenkins to automate project builds
- Cloud Fundamentals 
Use of the cloud rapid elasticity 


<a name="reqs"></a>
### Requirements 
The requirements of the project were as follows:

- An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
- This could also provide a record of any issues or risks that you faced creating your project.
- An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- The project must follow the Service-oriented architecture that has been asked for.
- The project must be deployed using containerisation and an orchestration tool.
- As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
- The project must make use of a reverse proxy to make your application accessible to the user.

<a name="approach"></a>
### Project Approach
To meet the projects SOA requirements I decided to create an application with 4 services that communicate with eachother to generate a random football player for the user. 

#### Service 1
The core service for the application where data recieved from other services is rendered into a Jinja2 template. Service 1 communicates with service 2, 3, 4 & presists some data in an MySQL database. Service 1 performs a **GET request on services 2, 3** and a **POST request on service 4**. The responses given by service 2, 3 & 4 are then used by service 1 to display back to the user via HTML and Jinja2 templating.

**routes located:  service1/application/routes.py**
```bash
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
```
I also added a generate button that can be used by the user to generate a random player

**routes located:  service1/application/templates/index.html**
```bash
<a href="{{ url_for('index')}}"><button>Generate</button></a>
```
#### Service 2
Service 2 generates a random player position. There a 3 position variations that can be assigned to the random player

**routes located:  service2/application/routes.py**
```bash
@app.route('/position', methods=['GET'])
def position():
    
    positions = ["Striker", "Midfield", "CenterBack"]
    position = positions[random.randrange(0,3)]

    return Response(position, mimetype="text/plain")
```

#### Service 3
Service 3 generate a random player team. There are 3 teams that can be assigned to the random player. 

#### Service 4