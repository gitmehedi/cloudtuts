#!/bin/bash


# Add route

sudo apt-get update -y
sudo apt-get install -y net-tools
sudo apt install openjdk-11-jdk -y
sudo java -version

sudo route add default gw 192.168.56.1


# Add host for cluster
sudo cat >> /etc/hosts <<EOF
192.168.56.60    jenkins
EOF

sudo sed -i 's/127.0.1.1/#127.0.1.1/g' /etc/hosts



touch /var/tmp/setup_hosts.sh