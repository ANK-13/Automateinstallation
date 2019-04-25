import subprocess
import os

def install(cmd):
        FNULL = open(os.devnull, 'w')
        try:
            out = subprocess.check_call(cmd,stdout=FNULL,shell=True)
            return [0,out]
        except subprocess.CalledProcessError as excp:                                                                                             
                return [excp.returncode,excp.output]


response=install("sudo apt-get install -y --force-yes python3")
if(response[0] != 0):
        print("could not install python3")

response=install("sudo apt-get install -y --force-yes python3-pip")
if(response[0] != 0):
        print("could not install python3-pip")

response = install("sudo apt-get install -y --force-yes nmap")
if(response[0] != 0):
	print("Could not install nmap")

response = install("sudo apt-add-repository -y ppa:ansible/ansible")
if(response[0] != 0):
    print("Could not install software-installer")

response = install("sudo apt-get update")
if(response[0] != 0):
    print("Could not install software")

response = install("sudo apt-get -y --force-yes install ansible")
if(response[0] != 0):
    print("Could not install software-installer")

response = install("sudo pip3 install virtualenv")
if(response[0] != 0):
    print("Could not install virtualenv")
	
reponse = install("sudo virtualenv -p /usr/bin/python3 env")
if(response[0] != 0):
	print("could not create a virtual env")

response = install("/root/project/Automateinstallation/env/bin/pip3 install -r requirements.txt")
if(response[0] != 0):
        print("could not install requirements file")

response = install("/root/project/Automateinstallation/env/bin/python3 app.py")
if(response[0] != 0):
        print("could not run project")


