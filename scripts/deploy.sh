#! /bin/bash

echo "Pulling images from Dockerhub.."
docker-compose pull
docker stack deploy -c docker-compose.yaml w9app