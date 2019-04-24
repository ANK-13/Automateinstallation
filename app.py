
from connexion.resolver import RestyResolver
import connexion
from logic.DiscoveredDevices import Devices
from flask_injector import FlaskInjector
from api.discoveredDevices import Device
from injector import Binder

# def configure(binder: Binder) -> Binder:
#     binder.bind(
#         Devices
#     )

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('IP_connexion.yaml')
    app.add_api('command_connexion.yaml')
    app.run(port=5000,debug=True)