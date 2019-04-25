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
        return output

    def createPlaybook():
        data = json.loads(request.data)
        package = data[0]
        print("Software toinstall: ",package)
        with open(Commands.getFileLocation("data/hosts"),"w") as f:
            f.write("[Devices]\n")
            for user in data[1:]:
                f.write("{0} ansible-ssh-user=root ansible-ssh-pass={1}\n".format(user["IP"],user["pass"]))
        playbook = ""
        if(package == "git"):
            playbook = Commands.getFileLocation("playbooks/git.yaml")
        elif(package == "java"):
            playbook = Commands.getFileLocation("playbooks/java.yaml")
        logs = Commands.executePlaybooks(playbook)
        with open(logs,"r") as l:
            flg = 0
            response = []
            for line in l.readlines():
                line = line.split()
                if(len(line)>=3 and line[0]=="PLAY" and line[1]=="RECAP"):
                    flg = 1
                    continue
                if(flg==1):
                    if(len(line)<3):
                        continue
                    print("================>",line)
                    tmp = {
                        "IP": line[0],
                        "ok": line[2].split("=")[1],
                        "changed": line[3].split("=")[1],
                        "unreachable": line[4].split("=")[1],
                        "failed": line[5].split("=")[1]
                    }
                    response.append(tmp)
        return response

