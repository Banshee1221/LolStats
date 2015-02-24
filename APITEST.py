import json

from riotwatcher import RiotWatcher, EUROPE_WEST

key = 'c2aa2be4-e00b-4a89-b622-3e17b67e1097'

summoner_name = "StirlingArcher69"

w = RiotWatcher(key)

s = w.get_summoner(name=summoner_name, region='euw')
sID = s['id']

stats = json.dumps(w.get_match_history(summoner_id=sID, region='euw'))
parsed = json.loads(stats)
print "Amount of games: "+str(json.dumps(parsed, indent=4, sort_keys=True).count("matchId"))
print "Data:"
print json.dumps(parsed, indent=4, sort_keys=True)


print "==== Match details for 1960675310 ===="
stats1 = json.dumps(w.get_match(1960675310, region='euw', include_timeline='true'))
parsed1 = json.loads(stats1)
print json.dumps(parsed1, indent=4, sort_keys=True)