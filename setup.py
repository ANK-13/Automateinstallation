import subprocess
import os

def install(cmd):
        FNULL = open(os.devnull, 'w')
        try:
            out = subprocess.check_call(cmd,stdout=FNULL,shell=True)
            return [0,out]
        except subprocess.CalledProcessError as excp:                                                                                             
                return [excp.returncode,excp.output]


response=install("sudo apt-get install -y  python3")
if(response[0] != 0):
        print("could not install python3")

response=install("sudo apt-get install -y  python3-pip")
if(response[0] != 0):
        print("could not install python3-pip")

response = install("sudo apt-get install -y  nmap")
if(response[0] != 0):
	print("Could not install nmap")

response = install("sudo apt-add-repository -y ppa:ansible/ansible")
if(response[0] != 0):
    print("Could not install software-installer")

response = install("sudo apt-get update")
if(response[0] != 0):
    print("Could not install software")

response = install("sudo apt-get -y  install ansible")
if(response[0] != 0):
    print("Could not install software-installer")

response = install("sudo pip3 install virtualenv")
if(response[0] != 0):
    print("Could not install virtualenv")

response = install("sudo apt-get install sshpass")
if(response[0] != 0):
    print("Could not install sshpass")
	
reponse = install("sudo virtualenv -p /usr/bin/python3 env")
if(response[0] != 0):
	print("could not create a virtual env")

response = install("./env/bin/pip3 install -r requirements.txt")
if(response[0] != 0):
        print("could not install requirements file")

response = install("./env/bin/python3 app.py")
if(response[0] != 0):
        print("could not run project")

response = install("sudo sed -i 's/#   StrictHostKeyChecking ask/StrictHostKeyChecking no/g' /etc/ssh/ssh_config")
if(response[0] != 0):
        print("could not edit ssh_config")

response = install('sudo rm -f /root/.ssh/id_rsa.pub')
response = install('sudo rm -f /root/.ssh/id_rsa')
response = install('sudo ssh-keygen -t rsa -f /root/.ssh/id_rsa -q -P ""')
if(response[0] != 0):
        print("WARNING: Could not generate Key")
