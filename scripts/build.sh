#! /bin/bash

docker-compose down --rmi all
docker-compose build
docker.withRegistry('https://registry.hub.docker.com', 'DOCKERHUB_CREDENTIALS'){
    image.push("${env.app_version}")}
docker-compose push