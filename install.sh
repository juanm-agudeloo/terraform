#!/bin/sh
sudo apt update
sudo apt install -y docker.io docker-compose
sudo apt install git -y
git clone https://github.com/juanm-agudeloo/terraform.git
cd terraform
sudo docker-compose up -d
