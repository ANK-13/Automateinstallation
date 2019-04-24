from flask_injector import inject
from logic.DiscoveredDevices import Devices
from datetime import datetime
import json

class Device:
    def __init__(self):pass

    def get():
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

    def getCidrIP():
        interface = netifaces.ifaddresses('eth0')
        ip = interface[netifaces.AF_INET][0]['addr']
        mask = interface[netifaces.AF_INET][0]['netmask']
        cidr = sum(bin(int(x)).count('1') for x in mask.split('.'))
        return ip+"/"+cidr
