#! /bin/bash

ssh -i ~/.ssh/ansible_id_rsa jenkins@leader << EOF
docker node ls
sudo docker node ls
EOF

