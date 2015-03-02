"""
LolWatcher is an
"""

# ==== Imports
import json
from riotwatcher import RiotWatcher, EUROPE_WEST

class main:

    def __init__(self, _APIkey, _sumName, _matchNo):

        # ==== Definitions
        self._APIkey = _APIkey                                                              # API key for developers
        self._summoner_name = _sumName                                                      # Name of LoL Summoner
        self._watcherObj = RiotWatcher(self._APIkey)                                        # riotwatcher data
        self._sumObj = self._watcherObj.get_summoner(name=self._summoner_name, region='euw')              # Data on Summoner
        self._sID = self._sumObj['id']                                                      # ID of Summoner
        self._match = _matchNo                                                               # ID of match to work with
        self._stats1 = json.dumps(self._watcherObj.get_match(self._match, region='euw', include_timeline='true'))
        self._parsed1 = json.loads(self._stats1)
        self._matchId = self._parsed1['matchId']
        self._mapId = self._parsed1['mapId']

    def getPeopleForMatch(self):

        _people = {}                                                                # ID | name

        for a in self._parsed1['participantIdentities']:
            _people[a['player']['summonerId']] = str(a['player']['summonerName'])

        return _people

    def getParticipantsForMatch(self):

        _participants = {}                                                          # number | ID

        for values in self._parsed1['participantIdentities']:
            _participants[values['participantId']] = values['player']['summonerId']

        return _participants

    def getEventsPerPerson(self):

        _eventsPerPerson = {}

        for count in range(10):
            _eventsPerPerson[str(count + 1)] = []

        for items in self._parsed1['timeline']['frames']:     # ignores wards
            try:
                tempList = items['events']
                for vals in tempList:
                    #if "participantId" in str(vals):
                    #    _eventsPerPerson[str(vals['participantId'])] = _eventsPerPerson[str(vals['participantId'])] + [vals]
                    if "killerId" in str(vals):
                        _eventsPerPerson[str(vals['killerId'])] = _eventsPerPerson[str(vals['killerId'])] + [vals]
            except KeyError:
                continue
                # print "skipped", str(items['participantFrames'])

        return _eventsPerPerson

    def getFramesPerPerson(self):

        _framesPerPerson = {}

        for count in range(10):
            _framesPerPerson[str(count + 1)] = []

        for values in self._parsed1['timeline']['frames']:
            for count in range(1, 11):
                tempDict = dict(values['participantFrames'][str(count)])
                _framesPerPerson[str(count)] = _framesPerPerson[str(count)] + [tempDict]

        return _framesPerPerson

#for key in _eventsPerPerson:
    #    print "Participant:", str(key)
    #    for events in _eventsPerPerson[key]:
    #        temp = json.dumps(events, indent=4, sort_keys=True)
    #        print temp

match = 1960675310
run = main('', "StirlingArcher69", match)
print "==== Match details for", str(match), "===="
print(json.dumps(run.getEventsPerPerson(), indent=4, sort_keys=True))