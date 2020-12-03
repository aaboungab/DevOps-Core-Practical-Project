#! /bin/bash

if (env.rollback == 'false'){
                            image1 = docker.build("aaboungab/service1")
                            image2 = docker.build("aaboungab/service2")
                            image3 = docker.build("aaboungab/service3")
                            image4 = docker.build("aaboungab/service4")
                            imagesql = docker.build("aaboungab/mysql")
                            imagenginx = docker.build("aaboungab/nginx")}
