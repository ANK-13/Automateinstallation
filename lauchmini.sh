#!/bin/bash
echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config
echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
sed -i "s/PermitRootLogin without-password/PermitRootLogin yes/g" /etc/ssh/sshd_config
service ssh restart
service sshd restart
echo root:root | chpasswd
sudo apt-get install -y python-minimal
