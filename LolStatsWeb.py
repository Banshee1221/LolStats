#!/usr/bin/python
# -*- coding: utf-8 -*-
# Imports

from __future__ import division
from flask import Flask, render_template
import os, json, glob, re, filecmp
from riotwatcher import RiotWatcher

watcherOb = RiotWatcher(str(raw_input("Enter API key: ")))

# LolStats
# The match history is a temporary solution to get this done quick,
# basically it just dumps a match history file every time instead of
# adding on to the current one. :(
origDir = os.getcwd()
_playerName = str(raw_input("Summoner Name: "))
_playerRegion = str(raw_input("Enter your region: "))
_playerData = ''
_playerID = 0
_playerHist = ''
if _playerRegion != '':
    _playerData = watcherOb.get_summoner(name=_playerName, region=_playerRegion)
    _playerID = int((watcherOb.get_summoner(name=_playerName, region=_playerRegion))['id'])
    _playerHist = watcherOb.get_match_history(summoner_id=_playerID, region=_playerRegion)
else:
    _playerData = watcherOb.get_summoner(name=_playerName)
    _playerID = int((watcherOb.get_summoner(name=_playerName))['id'])
    _playerHist = watcherOb.get_match_history(summoner_id=_playerID)

_playerMatches = []
for allVals in _playerHist['matches']:
    _playerMatches.append(allVals['matchId'])

#
#
#print json.dumps(_playerHist, indent=4)

_dir = str(os.getcwd())+"\\static\\json\\"

# Dir creation

def writer(_dir, _file, _data, _json):
    writeFile = open(str(_dir)+"\\"+str(_file), "w")
    if _json is True:
        writeFile.write(json.dumps(_data, indent=4))
    else:
        writeFile.write(_data)
    writeFile.close()


if not os.path.exists(_dir+str(_playerID)):
    os.makedirs(str(_dir+str(_playerID)))
    writer((str(_dir+str(_playerID))), "_playerData.json", _playerData, True)
    writer((str(_dir+str(_playerID))), "_playerHist1.json", _playerHist, True)
else:
    if not os.path.isfile(str(_dir+str(_playerID)+"\\_playerData.json")):
        writer((str(_dir+str(_playerID))), "_playerData.json", _playerData, True)
    if not os.path.isfile(str(_dir+str(_playerID)+"\\_playerHist1.json")):
        writer((str(_dir+str(_playerID))), "_playerHist1.json", _playerHist, True)
    elif os.path.isfile(str(_dir+str(_playerID)+"\\_playerHist1.json")):
        os.chdir(_dir+str(_playerID))
        temp = glob.glob("_playerHist*")
        inc = int(re.search(r'\d+', str(temp[-1])).group()) + 1
        writer((str(_dir+str(_playerID))), "_playerHist"+str(inc)+".json", _playerHist, True)
        if filecmp.cmp("_playerHist"+str(inc-1)+".json", "_playerHist"+str(inc)+".json") is True:
            os.remove("_playerHist"+str(inc)+".json")
        os.chdir(origDir)


if not os.path.exists(_dir+str(_playerID)+"\\matchData"):
    os.makedirs(_dir+str(_playerID)+"\\matchData")


os.chdir(_dir+str(_playerID))
for i in glob.glob("_playerHist*"):
    temp = json.load(open(i, 'r'))
    for vals in temp['matches']:
        if not os.path.isfile(str(_dir+str(_playerID)+"\\matchData\\"+str(vals['matchCreation'])+".json")):
            writer(str(_dir+str(_playerID)+"\\matchData\\"), str(vals['matchCreation'])+".json", watcherOb.get_match(match_id=vals['matchId'], include_timeline=True), True)
os.chdir(origDir)




#_playerName = "TheOddOne"
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