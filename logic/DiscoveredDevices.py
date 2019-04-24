import socket  
import netifaces 

class Devices(object):

    def __init__(self):pass

    @classmethod
    def getSample(self):
        return """[
        {
            "id": 1,
            "MACAddr": "json-server",
            "IPAddr": "typ"
        },
        {
            "id": 2,
            "MACAddr": "json-server",
            "IPAddr": "typicode"
        }
        ]
        """

    def getCidrIP():
        interface = netifaces.ifaddresses('eth0')
        ip = interface[netifaces.AF_INET][0]['addr']
        mask = interface[netifaces.AF_INET][0]['netmask']
        cidr = sum(bin(int(x)).count('1') for x in mask.split('.'))
        return ip+"/"+cidr

