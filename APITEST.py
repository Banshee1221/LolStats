import json

from riotwatcher import RiotWatcher, EUROPE_WEST

key = 'c2aa2be4-e00b-4a89-b622-3e17b67e1097'

summoner_name = "StirlingArcher69"

w = RiotWatcher(key)

s = w.get_summoner(name=summoner_name, region='euw')
sID = s['id']

match = 1960675310

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


for c in parsed1['timeline']['frames']:
    for count in range(1, 11):
        print count
        temp = _eventsPerPerson[str(count)]
        tempDict = dict(c['participantFrames'][str(count)])
        _eventsPerPerson[str(count)] = _eventsPerPerson[str(count)].append(tempDict)
        #temp = temp.append(c['participantFrames'][str(count)])
        #print temp
        #_eventsPerPerson[count] = temp
