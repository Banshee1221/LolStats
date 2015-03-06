__author__ = 'Eugene'

import os
import json
import glob
import re
import filecmp
from riotwatcher import RiotWatcher

class DataStore:

    def __init__(self, api, sumName, region):

        self.watcherOb = RiotWatcher(api)

        # LolStats
        # The match history is a temporary solution to get this done quick,
        # basically it just dumps a match history file every time instead of
        # adding on to the current one. :(

        self.origDir = os.getcwd()
        self._playerName = sumName
        self._playerRegion = region
        self._playerData = ''
        self._playerID = 0
        self._playerHist = ''
        if self._playerRegion != '':
            self._playerData = self.watcherOb.get_summoner(name=self._playerName, region=self._playerRegion)
            self._playerID = int((self.watcherOb.get_summoner(name=self._playerName, region=self._playerRegion))['id'])
            self._playerHist = self.watcherOb.get_match_history(summoner_id=self._playerID, region=self._playerRegion)
        else:
            self._playerData = self.watcherOb.get_summoner(name=self._playerName)
            self._playerID = int((self.watcherOb.get_summoner(name=self._playerName))['id'])
            self._playerHist = self.watcherOb.get_match_history(summoner_id=self._playerID)

        self._playerMatches = []
        for allVals in self._playerHist['matches']:
            self._playerMatches.append(allVals['matchId'])

        _dir = str(os.getcwd())+"\\static\\json\\"

        # Dir creation

        def writer(_dir, _file, _data, _json):
            writeFile = open(str(_dir)+"\\"+str(_file), "w")
            if _json is True:
                writeFile.write(json.dumps(_data, indent=4))
            else:
                writeFile.write(_data)
            writeFile.close()

        if not os.path.exists(_dir+str(self._playerID)):
            os.makedirs(str(_dir+str(self._playerID)))
            writer((str(_dir+str(self._playerID))), "_playerData.json", self._playerData, True)
            writer((str(_dir+str(self._playerID))), "_playerHist1.json", self._playerHist, True)
        else:
            if not os.path.isfile(str(_dir+str(self._playerID)+"\\_playerData.json")):
                writer((str(_dir+str(self._playerID))), "_playerData.json", self._playerData, True)
            if not os.path.isfile(str(_dir+str(self._playerID)+"\\_playerHist1.json")):
                writer((str(_dir+str(self._playerID))), "_playerHist1.json", self._playerHist, True)
            elif os.path.isfile(str(_dir+str(self._playerID)+"\\_playerHist1.json")):
                os.chdir(_dir+str(self._playerID))
                temp = glob.glob("_playerHist*")
                inc = int(re.search(r'\d+', str(temp[-1])).group()) + 1
                writer((str(_dir+str(self._playerID))), "_playerHist"+str(inc)+".json", self._playerHist, True)
                if filecmp.cmp("_playerHist"+str(inc-1)+".json", "_playerHist"+str(inc)+".json") is True:
                    os.remove("_playerHist"+str(inc)+".json")
                os.chdir(self.origDir)

        if not os.path.exists(_dir+str(self._playerID)+"\\matchData"):
            os.makedirs(_dir+str(self._playerID)+"\\matchData")

        os.chdir(_dir+str(self._playerID))
        for i in glob.glob("_playerHist*"):
            temp = json.load(open(i, 'r'))
            for vals in temp['matches']:
                if not os.path.isfile(str(_dir+str(self._playerID)+"\\matchData\\"+str(vals['matchId'])+".json")):
                    writer(str(_dir+str(self._playerID)+"\\matchData\\"), str(vals['matchId'])+".json", self.watcherOb.get_match(match_id=vals['matchId'], include_timeline=True), True)
        os.chdir(self.origDir)
