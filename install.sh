#!/bin/sh
sudo apt update
sudo apt install docker-compose -y
sudo apt install git -y
git clone https://github.com/usuario/proyecto
cd proyecto
sudo docker-compose up -d
