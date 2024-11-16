#!/bin/sh
sudo apt update
sudo apt install docker-compose -y
sudo apt install git -y
git clone https://github.com/juanm-agudeloo/terraform
cd terrform
sudo docker-compose up -d
