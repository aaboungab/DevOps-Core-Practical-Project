# ⚽ Football player generator ⚽ - change
## Week 9 Practical Project

## Author
### Anas Aboungab

### Links
- [Trello](https://trello.com/b/0Cc9TWJl/practical-qa-project)
- [Risk Assessment](https://docs.google.com/spreadsheets/d/1FCPe9_ZKv7dBet7Kun1iwqqojjbt0dE1ftpGjEZP5fs/edit#gid=0)

## Contents
- [Brief](#brief)
    - [Objective](#obj)
    - [Requirements](#reqs)
    - [Project Approach](#approach)
- [Architecture](#arch)
    - [Container level architecture](#cla)
    - [Service-Orientated architecture](#soa) 
    - [Application Infrastructure](#appinf)
    - [Entity Relationship Diagram](#erd)
- [Continuous Integration pipeline](#ci)
    - [CI pipeline - version 1](#ci1)
    - [CI pipeline - version 2](#ci2)
- [Testing](#test_)
    - [Service 1 test](#test_1)
    - [Service 2 & 3 test](#test_2/3)
    - [Service 4 test](#test_4)
- [Risk Assessment](#risks)
- [Project Planning & Tracking](#use_case)
- [Technologies used](#tech)
- [Successes](#suc)
- [Future Improvements](#improve)

<a name="brief"></a>
## Brief

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

The focus of this project was around **microservices** style architecture and how different this model is to a monolithic architectural style, which was the model used in the previous [DevOps core fundamental project](https://github.com/aaboungab/DevOps-Core-Fundamental-Project) for the QA training academy. 

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
To meet the projects model requirements, I decided to create an application with 4 services that communicate with eachother to generate a random football player for the user. 

#### Service 1
The core service is to perform a **GET request on services 2, 3** and a **POST request on service 4**. Service 1 communicates with service 2, 3, 4 & presists some data in a MySQL database.The responses given by service 2, 3 & 4 are then used by service 1 to display back to the user via HTML and Jinja2 templating.

**routes located:  service1/application/routes.py**
```bash
@app.route('/', methods=['GET','POST'])
def index():

    #get position
    position = requests.get("http://service2:5001/position")
    #get team name
    team = requests.get("http://service3:5002/team")
    #post player
    name = requests.post("http://service4:5003/name", data=info)
    info = str(position.text) + " " + str(team.text)

    return render_template('index.html', title='player team', position=position.text, team=team.text, info=info, name=name.text)
```
I also added a generate button that can be used by the user to generate a random player

**routes located:  service1/application/templates/index.html**
```bash
<a href="{{ url_for('index')}}"><button>Generate</button></a>
```
#### Service 2
Service 2 generates a random player position. There a 3 position variations that can be assigned to the random player. This service will send a G

**routes located:  service2/application/routes.py**
```bash
@app.route('/position', methods=['GET'])
def position():
    
    positions = ["Striker", "Midfield", "CenterBack"]
    position = positions[random.randrange(0,3)]

    return Response(position, mimetype="text/plain")
```

#### Service 3
Service 3 generates a random player team. There are 3 teams that can be assigned to the random player. 

**routes located:  service3/application/routes.py**
```bash
@app.route('/team', methods=['GET'])
def team():

    teams = ["Arsenal", "Chelsea", "Liverpool"]

    team = teams[random.randrange(0,3)]
    
    return Response(team, mimetype="text/plain")
```

#### Service 4
Service 4 is used to generate a random player depending on service 2 player position and service 3 player team. Service 4 will then return the player name back to service 1 as a POST response to display to the user. 

**routes located:  service4/application/routes.py**
```bash
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
```
<a name="arch"></a>
## Architecture
Application that utilises that benefits of micro-service architecture and containerisation

<a name="cla"></a>
### Container level architecture
Container level architecture was as follows:

<img src="/documentation/CLA.png" alt="" width="100%" height="100%"/>

<a name="soa"></a>
### Service-Orientated architecture 
Below is the service architecture of my application. 

<img src="/documentation/SOA diagram.png" alt="" width="100%" height="100%"/>

<a name="appinf"></a>
### Application Infrastructure
<img src="/documentation/infrastructure.png" alt="" width="100%" height="100%"/>

<a name="erd"></a>
### Entity Relationship Diagram
MySQL database was used to persist the generated data.

[CreateTables.sql](https://github.com/aaboungab/W9_-SoloProject/blob/master/CreateTables.sql)

<img src="/documentation/erd.png" alt="" width="100%" height="100%"/>

<a name="ci"></a>
## Continous Integration pipeline 
CI development practice was implemented into my project to integrate my code into a version control system (Github). My CI pipeline evolved throughout the duration of the project and below I will illustrate what changed. 

<a name="ci1"></a>
### CI pipeline - version 1
My pipeline initally used jenkins to automate testing, building & deploying my application via the Jenkinsfile. I used Jenkins webhook to trigger project builds when a commit is made into the master branch. At this stage I was using a multi-branch model to seperate my branches to then merge on github to be ready for deployment. 

<img src="/documentation/ci-1.png" alt="" width="100%" height="100%"/>

The below Jenkinsfile is a three-stage CI pipeline that I used. The test stage step used a script (test.sh) which will test services 1, 2, 3 and 4. The next stage would be building the application, this consisted of building docker images from the Dockerfiles in each service and pushing these images to Dockerhub. The final stage was deploying my application into the swarm cluster which required me to SSH into the leader (swarm-manager), clone down the Github repository, pull the images using the docker-compose.yaml file then deploying my application into the swarm. 

```bash
pipeline{
        agent any
        stages{
            stage('Test application'){
                steps{
                    sh "./scripts/test.sh"
                }
            }
            stage('Build docker images'){
                steps{
                    sh "./scripts/build.sh"
                }
            }
            stage('Deploy application'){
                steps{
                    sh "./scripts/deploy.sh"
                }
            }
        }
}
```

**CI pipeline version 1 - areas of improvement:**
- Configuration of the swarm cluster

The docker swarm cluster had to be configured manually in this version. My cluster consisted of 2 nodes which I had to SSH into to get the cluster up and running. This was quite inefficient as the configuration steps could have been automated. 

<a name="ci2"></a>
### CI pipeline - version 2
This version of the CI pipeline is an extension of the first but with a major configuration tool being added called Ansible. This made my CI pipeline much more lean and agile, Ansible took care of installing set of dependancies, docker, docker-compose across my cluster and initalising the swarm. First, I had to create an Ansible Inventory file to define the hosts and groups in my cluster. I then used the core feature Ansible playbboks that was used to automate the cluster configuration. Playbooks are yaml files that essentially contain a set of tasks for Ansible to complete. Ansible roles was used alongside the playbook to further specificy what needs to installed in each node. 

<img src="/documentation/ci-2.png" alt="" width="100%" height="100%"/>

My Jenkinsfile changed to add a new step **Ansible Swarm config** after building the docker images to setup swarm by adding the name of the vm into the ansible inventory file. 

```bash
pipeline{
        agent any
        stages{
            stage('Testing'){
                steps{
                    sh "./scripts/test.sh"
                }
            }
            stage('Building Images'){
                steps{
                    sh "./scripts/build.sh"
                }
            }
            stage('Ansible Swarm config'){
                steps{
                    sh "./scripts/ansible.sh"
                }
            }
            stage('Deploying App'){
                steps{
                    sh "./scripts/deploy.sh"
                }
            }
        }
    
}
```
[scripts](https://github.com/aaboungab/W9_-SoloProject/tree/master/scripts)

**CI pipeline version 2 - areas of improvement:**
- Jenkins pipeline stage builds notification

Jenkins provides useful plugins to send build notifications through email, slack or teams. Since I am working this project soley I did not require build notifications. However, if more individuals were involved in the project this can be a useful tool to add into the pipeline for the future. Allowing all developers/parties involved to keep track of the state of the application. 

<img src="/documentation/ci-3.png" alt="" width="100%" height="100%"/>

<a name="test_"></a>
## Testing
The service in my application were tested using Python libaries Pytest and Unittest.mock.  

<a name="test_1"></a>
### Service 1 test
Service 1 was test using unittest.mock library to enable me to mock responses that I would expect from services 2, 3 and 4. The method **patch** was used to change the functionality of the function to return a player name. This is then tested against the return data that would be expected from services 2, 3 and 4

[test_service_1.py](https://github.com/aaboungab/W9_-SoloProject/blob/master/service1/testing/test_service_1.py)

```bash
class TestResponse(TestBase):
    def test_page(self):
        with patch("requests.get") as v:
            with patch("requests.post") as p:
                v.return_value.text = "Arsenal"
                p.return_value.text = "Mesut Ozil"

                response = self.client.get(url_for('index'))
                self.assertIn(b'Your player is Mesut Ozil, they play in the Arsenal position for Arsenal', response.data)
```
<img src="/documentation/tests1.png" alt="" width="100%" height="100%"/>

<a name="test_2/3"></a>
### Service 2 & 3 tests
Services 2 and 3 ran basic pytests to ensure that the output of each service was in the correct format

**Service 2 test**: complete test can be found at [test_service_2.py](https://github.com/aaboungab/W9_-SoloProject/blob/master/service2/testing/test_service_2.py)
```bash
class TestResponse(TestBase):

    def test_striker_position(self):
        with patch('random.randrange') as r:
            r.return_value = 0
            response = self.client.get(url_for('position'))
            self.assertIn(b'Striker', response.data)
```
<img src="/documentation/tests2.png" alt="" width="100%" height="100%"/>

**Service 3 test**: complete test can be found at [test_service_3.py](https://github.com/aaboungab/W9_-SoloProject/blob/master/service3/testing/test_service_3.py)

```bash
class TestResponse(TestBase):
    def test_arsenal_team(self):
        with patch('random.randrange') as r:
            r.return_value = 0
            response = self.client.get(url_for('team'))
            self.assertIn(b'Arsenal', response.data)
```
<img src="/documentation/tests3.png" alt="" width="100%" height="100%"/>

<a name="test_4"></a>
### Service 4 test
Service 4 test also used unittest.mock library similar to service 1 to mock the responses from service 2 and 3. Service 4 also ran unit tests to ensure that the response data is as expected. 

**Service 4 test**: complete test can be found at [test_service_4.py](https://github.com/aaboungab/W9_-SoloProject/blob/master/service4/testing/test_service_4.py)

```bash
def test_chelsea_st(self):
        with patch('requests.get') as i:
            i.return_value.text = 'Chelsea'
            with patch('random.randrange') as r:
                    r.return_value = 'Striker'
                    response = self.client.post(
                        url_for('name'),
                        data = 'Striker Chelsea')
                    self.assertIn(b'Olivier Giroud', response.data)
```
<img src="/documentation/tests4.png" alt="" width="100%" height="100%"/>

<a name=risks></a>
## Risk Assessment
I have thought of a number of risks that my project may face and have categorised them below to analyse the risk, its impact, likelihood and the appropriate response to that risk. The risks can be seen as a combination of technical risks associate with the development side of the project and general risks that will directly or indirectly impact the project

[Excel version](https://docs.google.com/spreadsheets/d/1FCPe9_ZKv7dBet7Kun1iwqqojjbt0dE1ftpGjEZP5fs/edit#gid=0)
<img src="/documentation/Risks.png" alt="" width="100%" height="100%"/>

<a name="use_case"></a>
## Project Planning & Tracking
I used Trello as a planning tool to keep track of tasks and update what needs to be done or has been completed. 

My inital Trello board:
<img src="/documentation/trello-1.png" alt="" width="100%" height="100%"/>

My final Trello board:
<img src="/documentation/trello-2.png" alt="" width="100%" height="100%"/>

<a name="tech"></a>
## Technologies Used
* Database: GCP SQL Server
* Programming language: Python
* Framework: Flask
* Deployment: Gunicorn
* CI Server: Jenkins
* Test Reporting: Pytest, unittest.mock
* VCS: [Git](https://github.com/aaboungab)
* Project Tracking: [Trello](https://trello.com/b/0Cc9TWJl/practical-qa-project)
* Live Environment: GCP
* Containerization: Docker
* Configuration Management: Ansible
* Orchestration: Docker-compose

<a name="suc"></a>
## Successes
* Microservice Architecture
    - Docker/Docker-compose (containerisation)
* Jenkins
    - plugins
    - credentials 
    - rolling updates
* Linux
    - User Administration
    - Ownership
    - Sudoers 
    - SSH

<a name="improve"></a>
## Future Improvements
* Adding an Email server into my Jenkins CI pipeline to send build notifications
* Use of Database to show the user the history of generated players and most recent player generated
* Implementing the use of JSON to increase data parsing speed
* I believe that my attempt at nginx was incorrect below is my second attempt

```bash
events{}
http {
    server {
        listen 80;
        location / {
            proxy_pass http://service1:5000/;
        }
    }
}
```

* Use of Enviornment variables in my project


