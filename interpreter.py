__author__ = 'markgrivainis'

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Imports

import json
import os
from parse import ReadPlayer

class Interpreter():
    origDir = os.getcwd()
    def __init__(self, playerId):
        self.playerId = playerId
        self.playerMatches = ReadPlayer(playerId)


#############################
#
#   need to put this in a class of its own
#   but for now it will do
#   still need to add functionality for won/lost dragon/baron
#   would like to add a average gold option across all games
#   need to add lane
#   not sure if I should add the per match data to this dict, total[kills, assists, deaths, gold, etc...]
#
#   data = {'matches' : [ints],
#           'games' [
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
#           }
#############################
    def getSpecificMatchData(self, array):

        playerId = 0
        lastTime = 0;
        data = {'games': [], 'matches': []}
        #arrays = json.loads(array)
        print array
        if array != None:
            for i in array:
                currentGame = self.playerMatches.getOneMatch(i)
                if currentGame['matchDuration'] > lastTime:
                    lastTime = currentGame['matchDuration']
                temp = {'matchId': currentGame['matchId'], 'kills': [], 'deaths': [], 'assists': [], 'dragons': [], 'barons': []}
                for k in currentGame['participantIdentities']:
                    if k['player']['summonerId'] == self.playerId:
                        playerId = k['participantId']
                for j in currentGame['timeline']['frames']:
                    if 'events' in j:
                        for a in j['events']:
                            if a['eventType'] == "CHAMPION_KILL" and a['killerId'] == playerId:
                                temp['kills'].append({'timestamp': a['timestamp']/1000, 'position': a['position']})
                            if a['eventType'] == "CHAMPION_KILL" and a['victimId'] == playerId:
                                temp['deaths'].append({'timestamp': a['timestamp']/1000, 'position': a['position']})
                            if not (not (a['eventType'] == "CHAMPION_KILL") or not ('assistingParticipantIds' in a) or not (
                                playerId in a['assistingParticipantIds'])):
                                temp['assists'].append({'timestamp': a['timestamp']/1000, 'position': a['position']})
                            if a['eventType'] == "ELITE_MONSTER_KILL" and a['monsterType'] == "DRAGON":
                                temp['dragons'].append({'timestamp': a['timestamp']/1000, 'position': a['position'],
                                                       'won': (a['killerId'] <=5 and playerId <= 5) or (a['killerId'] >5 and playerId > 5)})
                            if a['eventType'] == "ELITE_MONSTER_KILL" and a['monsterType'] == "BARON":
                                temp['barons'].append({'timestamp': a['timestamp']/1000, 'position': a['position'],
                                                      'won': (a['killerId'] <=5 and playerId <= 5) or (a['killerId'] >5 and playerId > 5)})
                data['games'].append(temp)
                data['matches'].append(currentGame['matchId'])
            data['longestTime'] = lastTime
            return data


    def getOverview(self):

        os.chdir(self.origDir+"/static/json/")

        temp_champs = dict(json.load(open("champions.json", "r")))
        os.chdir(self.origDir)
        playerMatches = ReadPlayer(self.playerId)
        var = playerMatches.getAllPlayerMatches()
        data = []
        for i in reversed(var):
            for k in i['participantIdentities']:
                if k['player']['summonerId'] == self.playerId:
                    id = k['participantId']
                    temp = {'matchId': i['matchId'],
                            'kills': i['participants'][id-1]['stats']['kills'],
                            'deaths': i['participants'][id-1]['stats']['deaths'],
                            'assists': i['participants'][id-1]['stats']['assists'],
                            'lane': i['participants'][id-1]['timeline']['lane'],
                            'gold': i['participants'][id-1]['stats']['goldEarned'],
                            'minionsKilled': i['participants'][id-1]['stats']['minionsKilled'] +
                                             i['participants'][id-1]['stats']['neutralMinionsKilled'],
                            'matchDuration': i['matchDuration'],
                            'winner': i['participants'][id-1]['stats']['winner'],
                            'champion': temp_champs['data'][str(i['participants'][id-1]['championId'])]['key']}
                    data.append(temp)
        return data