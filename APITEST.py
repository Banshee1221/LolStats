import json

from riotwatcher import RiotWatcher, EUROPE_WEST

key = 'c2aa2be4-e00b-4a89-b622-3e17b67e1097'

summoner_name = 'Sterlingarcher69'

w = RiotWatcher(key)

s = w.get_summoner(name=summoner_name)
sID = s['id']

stats = json.dumps(w.get_recent_games(sID))
parsed = json.loads(stats)
print json.dumps(parsed, indent=4, sort_keys=True)
