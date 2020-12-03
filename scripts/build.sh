#! /bin/bash
docker --version
docker-compose down --rmi all
docker-compose pull
docker-compose build
