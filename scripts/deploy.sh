#! /bin/bash

ssh -i ~/.ssh/ansible_id_rsa jenkins@leader << EOF
sudo docker node ls
git clone https://github.com/aaboungab/W9_-SoloProject.git
cd W9_-SoloProject
docker pull aaboungab/service1:s1
docker pull aaboungab/service2:s2
docker pull aaboungab/service3:s3
docker pull aaboungab/service4:s4
sudo docker stack deploy -c docker-compose.yaml w9app
EOF

