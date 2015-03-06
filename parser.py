__author__ = 'Eugene'

import os
import json


class ParsePlayer:

    loc = os.getcwd()
    playerId = 0

    def __init__(self, playerId):
        os.chdir(self.loc+"\\static\\json\\"+str(playerId))
        self.playerId = playerId

    def getPlayerData(self):
        jsonDump = json.load(open("_playerData.json", "r"))
        return dict(jsonDump)


test = ParsePlayer(60783)
#print test.getPlayerData()['id']