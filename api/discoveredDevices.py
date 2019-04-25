from flask_injector import inject
from logic.DiscoveredDevices import Devices
from datetime import datetime
import netifaces
import json
import subprocess

class Device:
    def __init__(self):pass
    
    @classmethod
    def get(self):
        return json.loads("""[
        {
            "id": 1,
            "MACAddr": "json-server",
            "IPAddr": "typicode"
        },
        {
            "id": 2,
            "MACAddr": "json-server",
            "IPAddr": "typicode"
        }
        ]
        """)

    @classmethod
    def getCidrIP(self,card):
        try:
            interface = netifaces.ifaddresses(card)
            ip = interface[netifaces.AF_INET][0]['addr']
            mask = interface[netifaces.AF_INET][0]['netmask']
            cidr = sum(bin(int(x)).count('1') for x in mask.split('.'))
            return str(ip)+"/"+str(cidr)
        except ValueError:
            return 'Sorry Invalid Interface', 406
    
    @classmethod
    def execIt(self,cmd):
        try:
            out = subprocess.check_output(cmd, shell=True).decode("utf-8")
            return [0,out]                 
        except subprocess.CalledProcessError as excp:                                                                                                   
                return [excp.returncode,excp.output]


    def discoverDevices(name):
        cidr = Device.getCidrIP(name)
        if(cidr[1]==406):
            return cidr
        print("Discovering Devices for follwoing subnet: ",cidr)
        response = Device.execIt("nmap -sP {0}".format(cidr))
        response = Device.execIt("arp -a -i {0}".format(name))
        devices = []
        if(response[0] == 0):
            id = 1
            for device in response[1].split("\n"):
                data = device.split(" ")
                if(len(data)<4):
                    continue
                ip = data[1].strip("(").strip(")")
                mac = data[3]
                hostname = data[0]
                data = {
                    "id": id,
                    "MACAddr": mac,
                    "IPAddr": ip,
                    "Hostname": hostname
                }
                devices.append(data)
                id+=1
            return devices
        else:
            return "Could not find Devices", 501

    def discoverDevicesNMap(name):
        cidr = Device.getCidrIP(name)
        if(cidr[1]==406):
            return cidr
        print("Discovering Devices for follwoing subnet: ",cidr)
        response = Device.execIt("sudo nmap -sP {0}".format(name))
        devices = []
        if(response[0] == 0):
            id = 1
            for device in response[1].split("\n"):
                data = device.split(" ")
                if(len(data)<4):
                    continue
                ip = data[1].strip("(").strip(")")
                mac = data[3]
                hostname = data[0]
                data = {
                    "id": id,
                    "MACAddr": mac,
                    "IPAddr": ip,
                    "Hostname": hostname
                }
                devices.append(data)
                id+=1
            return devices
        else:
            return "Could not find Devices", 501
        



