#!/usr/bin/python
# -*- coding: utf-8 -*-
# Imports

from __future__ import division
from flask import Flask, render_template, request, url_for, redirect, jsonify
import os, json, glob, re, filecmp
from store import DataStore
from interpreter import Interpreter

regionMappings = {"br": "Brazil",
                  "eune": "EuropeNordicEast",
                  "euw": "EuropeWest",
                  "lan": "LatinAmericaNorth",
                  "las": "LatinAmericaSouth",
                  "na": "NorthAmerica",
                  "oce": "Oceania",
                  "kr": "Korean",
                  "ru": "Russia",
                  "tr": "Turkey"}
inv_regionMappings = {'Turkey': 'tr',
                      'Brazil': 'br',
                      'EuropeNordicEast': 'eune',
                      'NorthAmerica': 'na',
                      'LatinAmericaSouth': 'las',
                      'Oceania': 'oce',
                      'LatinAmericaNorth': 'lan',
                      'EuropeWest': 'euw',
                      'Korean': 'kr',
                      'Russia': 'ru'}
playerId = 0
var = None

# api = (str(raw_input("Enter API key: ")))
# name = (str(raw_input("Summoner Name: ")))
# region = (str(raw_input("Region: ")))
# #
# DataStore(api, name, region)
# var = Interpreter(60783)
# print json.dumps(var.getOverview(), indent=4)
# print json.dumps(var.getSpecificMatchData([1755845428, 1755824402, 1755800718]), indent=4)

#run = main(str(raw_input('Enter API Key: ')), _playerName, 1997209490, 'na', _rankedType="ranked")
#
#
#
#
# def sortEvents(personID):
#     event = []
#     x = []
#     y = []
#     time = []
#     _events = run.getEventsPerPerson()
#   #  _events1 = run1.getEventsPerPerson()
#  #   _events2 = run2.getEventsPerPerson()
#
#   #  templist = [_events, _events1, _events2]
#    # for items in templist:
#     for events in _events[str(personID)]:
#         if 'position' in events:
#             event.append(events['eventType'])
#             x.append(((int(events['position']['x'])*14990 / 14820 - 120)*512 / 14990))
#             y.append(512 - ((int(events['position']['y'])*15100 / 14881 - 120)*512 / 15040))
#             time.append(events['timestamp'])
#     for i in range(len(event)):
#         event[i] = str(event[i]).replace("u", "")
#     print x, y
#     return event, x, y, time
#


# Flask
app = Flask(__name__)

@app.route('/')
def home():
    #event, x, y, time = sortEvents(6)
    return render_template('search.html')  # ('home.html', events=event, x=x, y=y, time=time)

@app.route('/', methods=['POST'])
def home_post():
    sumName = ''
    regID = ''
    if request.method == 'POST':
        temp = request.form
        sumName = temp['InputName']
        regID = temp['regionSelect']
    #return stats(sumName, str(regID).lower())
    return redirect(url_for('stats', name=sumName, region=regionMappings[regID.lower()]))

@app.route('/stats/<region>/<name>', methods=['GET'])
def stats(name, region):
    newReg = inv_regionMappings[region]
    print name, newReg
    obj = DataStore('43e873ea-c59b-4e3c-95dd-82ac46f093e2', name, newReg)
    print obj
    ID = obj.getPlayerID()
    print ID
    global var
    var = Interpreter(ID)
    o = var.getOverview()
    s = var.getSpecificMatchData([])
    #print json.dumps(var.getOverview(), indent=4)
    #print var.getSpecificMatchData([1749310367, 1749340557])


    return render_template('stats.html', playername=name, region=region, jsonData=o, matchData=s)

@app.route('/stats/<region>/<name>', methods=['POST'])
def stats2(name, region):
    ar = request.json
    s = var.getSpecificMatchData(ar['1'])
    print jsonify(s)

    return jsonify(matchData2=s)

# with app.test_request_context():
#     print url_for('index')
#     print url_for('stats')

# def home():
#     #event, x, y, time = sortEvents(6)
#     return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
