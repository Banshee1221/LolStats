####
#
#
#
####

# ==== Imports
import json
from riotwatcher import RiotWatcher, EUROPE_WEST

# ==== Definitions
_APIkey = str(raw_input("Enter API Key: "))                                     # API key for developers
w = RiotWatcher(_APIkey)                                                        # riotwatcher data
summoner_name = "StirlingArcher69"                                              # Name of LoL Summoner
s = w.get_summoner(name=summoner_name, region='euw')                            # Data on Summoner
#sID = s['id']                                                                   # ID of Summoner
match = 1960675310                                                              # ID of match to work with



print "==== Match details for", str(match), "===="
stats1 = json.dumps(w.get_match(match, region='euw', include_timeline='true'))
parsed1 = json.loads(stats1)
#print json.dumps(parsed1, indent=4, sort_keys=True)
#for key, value in parsed1.items():
#    print key, value

# pretty print
_matchId = parsed1['matchId']

_mapId = parsed1['mapId']

_people = {}                                                                # ID | name

for a in parsed1['participantIdentities']:
    _people[a['player']['summonerId']] = str(a['player']['summonerName'])

_participants = {}                                                          # number | ID

for b in parsed1['participantIdentities']:
    _participants[b['participantId']] = b['player']['summonerId']

_eventsPerPerson = {}

for count in range(10):
    _eventsPerPerson[str(count + 1)] = []

for items in parsed1['timeline']['frames']:     # ignores wards
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

_framesPerPerson = {}

for count in range(10):
    _framesPerPerson[str(count + 1)] = []


for c in parsed1['timeline']['frames']:
    print c
    for count in range(1, 11):
        temp = _framesPerPerson[str(count)]
        tempDict = dict(c['participantFrames'][str(count)])
        _framesPerPerson[str(count)] = _framesPerPerson[str(count)] + [tempDict]


#for key in _eventsPerPerson:
#    print "Participant:", str(key)
#    for events in _eventsPerPerson[key]:
#        temp = json.dumps(events, indent=4, sort_keys=True)
#        print temp