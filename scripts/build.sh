#! /bin/bash
docker --version
sudo docker-compose down --rmi all
sudo docker-compose pull
sudo docker-compose build