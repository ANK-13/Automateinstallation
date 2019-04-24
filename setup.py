import subprocess

def installPackages(cmd):
    try:
            out = subprocess.check_output(cmd, shell=True).decode("utf-8")
            return [0,out]                 
        except subprocess.CalledProcessError as excp:                                                                                                   
                return [excp.returncode,excp.output]

response = installPackages("sudo apt -y install python3")
if(response[0] != 0):
    print("Could not install python3")

response = installPackages("sudo apt -y install python3-pip")
if(response[0] != 0):
    print("Could not install python3-pip")

response = installPackages("sudo apt-add-repository ppa:ansible/ansible")
if(response[0] != 0):
    print("Could not install software")

response = installPackages("sudo apt-get update")
if(response[0] != 0):
    print("Could not install software")

response = installPackages("sudo apt-get install ansible")
if(response[0] != 0):
    print("Could not install Ansible")