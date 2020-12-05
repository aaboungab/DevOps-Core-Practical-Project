#! /bin/bash

ssh -i ~/.ssh/ansible_id_rsa jenkins@leader << EOF
sudo docker node ls
sudo docker stack deploy -c docker-compose.yaml w9app
EOF

