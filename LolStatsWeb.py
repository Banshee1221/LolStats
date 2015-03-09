#!/usr/bin/python
# -*- coding: utf-8 -*-
# Imports

from __future__ import division
from flask import Flask, render_template
import os, json, glob, re, filecmp
from riotwatcher import RiotWatcher
from store import DataStore
from parser import ReadPlayer

# api = (str(raw_input("Enter API key: ")))
# name = (str(raw_input("Summoner Name: ")))
# region = (str(raw_input("Region: ")))

#DataStore(api, name, region)
#############################
#
#   need to put this in a class of its own
#   but for now it will do
#   still need to add functionality for won/lost dragon/baron
#   would like to add a average gold option across all games
#   need to add lane
#   not sure if I should add the per match data to this dict, total[kills, assists, deaths, gold, etc...]
#
#   data = {'games' [
#               'matchId' : int
#               'kills' : [
#                   'timestamp': int
#                   'position': {'x' : int, 'y': int}
#               ]
#               'assists' : [
#                   'timestamp': int
#                   'position': {'x' : int, 'y': int}
#               ]
#               'deaths' : [
#                   'timestamp': int
#                   'position': {'x' : int, 'y': int}
#               ]
#               'dragons' : [
#                   'timestamp': int
#                   'position': {'x' : int, 'y': int}
#               ]
#               'barons' : [
#                   'timestamp': int
#                   'position': {'x' : int, 'y': int}
#               ]
#
#############################
joMa = ReadPlayer('19660288')
var = joMa.getAllPlayerMatches()
id = 0
data = {'games': []}
for i in var:
    temp = {'matchId': i['matchId'], 'kills': [], 'deaths': [], 'assists': [], 'dragons': [], 'barons': []}
    for k in i['participantIdentities']:
        if k['player']['summonerId'] == 19660288:
            id = k['participantId']
    for j in i['timeline']['frames']:
        if 'events' in j:
            for a in j['events']:
                if a['eventType'] == "CHAMPION_KILL" and a['killerId'] == id:
                    temp['kills'].append({'timestamp': a['timestamp'], 'position': a['position']})
                if a['eventType'] == "CHAMPION_KILL" and a['victimId'] == id:
                    temp['deaths'].append({'timestamp': a['timestamp'], 'position': a['position']})
                if not (not (a['eventType'] == "CHAMPION_KILL") or not ('assistingParticipantIds' in a) or not (
                    id in a['assistingParticipantIds'])):
                    temp['assists'].append({'timestamp': a['timestamp'], 'position': a['position']})
                if a['eventType'] == "ELITE_MONSTER_KILL" and a['monsterType'] == "DRAGON":
                    temp['dragons'].append({'timestamp': a['timestamp'], 'position': a['position']})
                if a['eventType'] == "ELITE_MONSTER_KILL" and a['monsterType'] == "BARON":
                    temp['dragons'].append({'timestamp': a['timestamp'], 'position': a['position']})
    data['games'].append(temp)
print json.dumps(data, indent=4)
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
# # Flask
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     event, x, y, time = sortEvents(6)
#     return render_template('home.html', events=event, x=x, y=y, time=time)
#
# if __name__ == '__main__':
#     app.run()