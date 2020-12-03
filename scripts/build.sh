#! /bin/bash

docker login
docker-compose down --rmi all
docker-compose build
docker-compose push