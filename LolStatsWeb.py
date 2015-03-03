# -*- coding: utf-8 -*-
# Imports

from __future__ import division
from flask import Flask, render_template, jsonify, request
import requests
import json
from main import main


# LolStats

run = main(str(raw_input('Enter API Key: ')), "StirlingArcher69", 1997209490)

def sortEvents(personID):
    coords = []
    event = []
    x = []
    y = []
    time = []
    _events = run.getEventsPerPerson()
    for events in _events[str(personID)]:
        if 'position' in events:
            event.append(events['eventType'])
            x.append((int(events['position']['x'])*14990 / 14820 - 120)*512 / 14990)
            y.append((int(events['position']['y'])*15100 / 14881 - 120)*512 / 15040)
            coords.append(((int(events['position']['x'])*14990 / 14820 - 120)*512 / 14990, (int(events['position']['y'])*15100 / 14881 - 120)*512 / 15040))
            time.append(events['timestamp'])
    for i in range(len(event)):
        event[i] = str(event[i]).replace("u", "")
    print coords

    return event, x, y, time

# Flask
app = Flask(__name__)

@app.route('/')
def home():
    event, x, y, time = sortEvents(6)
    return render_template('home.html', events=event, x=x, y=y, time=time)

if __name__ == '__main__':
    app.run()