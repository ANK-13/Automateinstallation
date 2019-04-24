from flask import request
import json
import os

class Commands:

    def __init__(self):pass

    @classmethod
    def getFileLocation(self):
        dir = os.path.dirname(__file__)
        filepath = "../data/hosts"
        relpath = os.path.join(dir,filepath)
        return relpath
    
    # @classmethod
    # def sendToEts():

    #     Commands.getFileLocation()

    def createPlaybook():
        data = json.loads(request.data)
        with open(Commands.getFileLocation(),"w") as f:
            f.write("[Devices]\n")
            for user in data:
                f.write("{0} ansible-ssh-user=root ansible-ssh-pass={1}\n".format(user["IP"],user["pass"]))

        return "All ok"

