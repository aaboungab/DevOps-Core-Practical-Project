#! /bin/bash

ssh -i .ssh/ansible_id_rsa jenkins@leader
git clone https://github.com/aaboungab/W9_-SoloProject.git
cd W9_-SoloProject
docker stack deploy -c docker-compose.yaml w9app
