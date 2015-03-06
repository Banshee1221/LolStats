__author__ = 'Eugene'

import os
import glob
import json


class ParsePlayer:

    loc = os.getcwd()
    playerId = 0

    def __init__(self, playerId):
        os.chdir(self.loc+"\\static\\json\\"+str(playerId))
        self.playerId = playerId

    def getPlayerData(self):
        os.chdir(self.loc)
        return dict(json.load(open("_playerData.json", "r")))

    def getPlayerHist(self):
        amount = glob.glob("_playerHist*")
        temp = []
        if len(amount) > 1:
            for items in amount:
                temp.append(dict(json.load(open(items, "r"))))
            os.chdir(self.loc)
            return temp
        else:
            os.chdir(self.loc)
            return dict(json.load(open(amount[0], "r")))

    def getAllPlayerMatches(self):
        os.chdir(self.loc+"\\static\\json\\"+str(self.playerId)+"\\matchData")
        amount = glob.glob("*")
        temp = []
        if len(amount) > 1:
            for items in amount:
                temp.append(dict(json.load(open(items, "r"))))
            os.chdir(self.loc)
            return temp
        else:
            os.chdir(self.loc)
            return dict(json.load(open(amount[0], "r")))

    def getOneMatch(self, matchId):
        os.chdir(self.loc+"\\static\\json\\"+str(self.playerId)+"\\matchData")
        return dict(json.load(open(str(matchId)+".json"), "r"))


#test = ParsePlayer(60783)
#print test.getAllPlayerMatches()