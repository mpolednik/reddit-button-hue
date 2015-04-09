import threading
import requests
import json

class NUPnPDiscoveryThread(threading.Thread):

    def __init__(self, bridges):
        super(NUPnPDiscoveryThread, self).__init__()

        self.bridges = bridges

    def run(self):
        self.bridges.add(
            json.loads(
                requests.get(
                    'https://www.meethue.com/api/nupnp').text)[0]['internalipaddress'])
