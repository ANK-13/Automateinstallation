from flask import request
import json
import os
import subprocess

class Commands:

    def __init__(self):pass

    @classmethod
    def getFileLocation(self,customFile):
        dir = os.path.dirname(__file__)
        filepath = "../{0}".format(customFile)
        relpath = os.path.join(dir,filepath)
        return relpath
    
    @classmethod
    def execIt(self,cmd):
        try:
            out = subprocess.check_output(cmd, shell=True).decode("utf-8")
            return [0,out]                 
        except subprocess.CalledProcessError as excp:                                                                                                   
                return [excp.returncode,excp.output]

    @classmethod
    def executePlaybooks(self,playbook):
        hosts = Commands.getFileLocation("data/hosts")
        output = Commands.getFileLocation("data/output")
        cmd = "ansible-playbook -i {0} {1} > {2}".format(hosts,playbook,output)
        Commands.execIt(cmd)

    def createPlaybook():
        package = request.headers["Package"]
        data = json.loads(request.data)
        with open(Commands.getFileLocation("data/hosts"),"w") as f:
            f.write("[Devices]\n")
            for user in data:
                f.write("{0} ansible-ssh-user=root ansible-ssh-pass={1}\n".format(user["IP"],user["pass"]))
        
        if(package == "git"):
            playbook = Commands.getFileLocation("playbooks/git.yaml")
        elif(package == "java"):
            playbook = Commands.getFileLocation("playbooks/java.yaml")
        Commands.executePlaybooks(playbook)
        return package

