import signal
import websocket
import time
import json
import threading


class ButtonMonitor(threading.Thread):

    def __init__(self, lasttick):
        super(ButtonMonitor, self).__init__()

        self.lasttick = {}
        self.connection = \
            websocket.create_connection(
                'wss://wss.redditmedia.com/thebutton?h='
                'a5060ba96b640352441dae3255b9199a250b15d6&e=1428660041')

    def run(self):
        while 1:
            self.lasttick = json.loads(self.connection.recv())
            print self.lasttick
            time.sleep(0.3)


if __name__ == '__main__':
    lasttick = {}
    monitor = ButtonMonitor(lasttick)
    monitor.start()
