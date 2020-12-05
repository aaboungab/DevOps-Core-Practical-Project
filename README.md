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
