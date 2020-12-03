#! /bin/bash

echo "Pulling images from Dockerhub.."
docker stack deploy -c docker-compose.yaml w9app