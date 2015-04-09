import socket
import threading

MESSAGE = '\r\n'.join(['M-SEARCH * HTTP/1.1',
                       'Host: 239.255.255.250:1900',
                       'Man: "ssdp:discover"',
                       'ST: urn:schemas-upnp-org:device:Basic:1',
                       'MX: 3'])

ADDRESS = '239.255.255.250'
PORT = 1900


class UPnPDiscoveryThread(threading.Thread):

    def __init__(self, bridges, retries=5, timeout=2):
        super(UPnPDiscoveryThread, self).__init__()

        socket.setdefaulttimeout(timeout)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.retries = retries
        self.bridges = bridges

    def run(self):
        for _ in range(self.retries):
            self.sock.sendto(MESSAGE, (ADDRESS, PORT))
            data = self.sock.recv(1024)
            if not data:
                continue
            else:
                d = {}
                for line in data.split('\r\n'):
                    delimiter = line.find(':')
                    if delimiter != -1:
                        d[line[0:delimiter]] = line[delimiter+2:]

                location = d['LOCATION'][7:d['LOCATION'].find(':', 7)]
                self.bridges.add(location)
