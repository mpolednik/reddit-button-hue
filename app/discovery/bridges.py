import threading
import upnp
import nupnp


class DiscoveryThread(threading.Thread):

    def __init__(self, bridges):
        super(DiscoveryThread, self).__init__()
        self.bridges = bridges

        self.upnp_thread = upnp.UPnPDiscoveryThread(self.bridges)
        self.nupnp_thread = nupnp.NUPnPDiscoveryThread(self.bridges)

    def run(self):
        self.upnp_thread.start()
        self.nupnp_thread.start()
        self.upnp_thread.join()
        self.nupnp_thread.join()


def discover():
    bridges = set()
    discovery_thread = DiscoveryThread(bridges)
    discovery_thread.start()
    discovery_thread.join()

    return bridges
