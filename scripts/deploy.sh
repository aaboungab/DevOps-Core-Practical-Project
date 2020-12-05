#! /bin/bash

ssh -i ~/.ssh/ansible_id_rsa jenkins@leader << EOF
sudo docker node ls
git clone https://github.com/aaboungab/W9_-SoloProject.git
sudo docker stack deploy -c docker-compose.yaml w9app
EOF

