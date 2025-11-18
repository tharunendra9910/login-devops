#!/bin/bash
sudo apt update -y
sudo apt install -y zip unzip nginx
sudo rm -rf /var/www/html/
sudo git clone https://github.com/tharunendra9910/login-devops.git /var/www/html/
