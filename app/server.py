from discovery import bridges
from client import reddit
import requests
import json
import time
import math

time_to_color = {
    0: [0.69, 0.32],
    1: [0.71, 0.35],
    2: [0.46, 0.46],
    3: [0.40, 0.51],
    4: [0.17, 0.04],
    5: [0.220, 0.060]}


def run():
    br = list(bridges.discover())[0]
    last = {}
    monitor_thread = reddit.ButtonMonitor(last)
    lights = json.loads(requests.get('http://{}/api/newdeveloper/lights'.format(br)).text)
    monitor_thread.start()

    current_flair = 5

    while 1:
        print last
        try:
            current_flair = math.floor((last['tick']['payload']['seconds_left'] - 2) / 10)
        except:
            time.sleep(0.3)
            continue
        else:
            for light in lights:
                requests.put('http://{}/api/newdeveloper/lights/{}/state'.format(br, light), data='{"xy": [%s,%s]}' % (time_to_color[current_flair][0], time_to_color[current_flair][1]))
            time.sleep(0.3)

if __name__ == '__main__':
    run()
