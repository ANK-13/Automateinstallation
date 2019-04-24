from flask_injector import inject
from logic.DiscoveredDevices import Devices
from datetime import datetime

class Device:
    # def __init__(self,id: str,name: str,Org: str,date: datetime):
    #     self.id = id
    #     self.name = name
    #     self.Org = Org
    #     self.date= date

    # def toJson(self):
    #     return """
    #         {
    #             "id": {0},
    #             "name": {1},
    #             "Org": {2},
    #             "date": {3}
    #         }
    #     """.format(self.id,self.name,self.Org,self.date)
    
    @inject(data_provider=Devices)
    def get(data_provider: Devices):
        return data_provider.getCidrIP()