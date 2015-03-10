__author__ = 'Eugene'

from riotwatcher import RiotWatcher, EUROPE_WEST
import json

_watcherObj = RiotWatcher(str(raw_input("API: ")))
print _watcherObj.get_champion(64)
# _sumObj = _watcherObj.get_summoner(name='TheOddOne', region='na')
# print _sumObj
# #print json.dumps(_watcherObj.get_recent_games(summoner_id=_sumObj['id'], region='euw'), indent=4)
#
# #_parsed=_watcherObj.get_match_history(summoner_id=_sumObj['id'],region='na')
# #print json.dumps(_parsed, indent=4)
# _parsed1=_watcherObj.get_match(match_id=1749368438, region='na', include_timeline=True)
# print json.dumps(_parsed1, indent=4)

# _eventsPerPerson = {}
#
# for count in range(10):
#     _eventsPerPerson[str(count + 1)] = []
#
# for items in _parsed1['timeline']['frames']:     # ignores wards
#     try:
#         tempList = items['events']
#         for vals in tempList:
#            #if "participantId" in str(vals):
#            #    _eventsPerPerson[str(vals['participantId'])] = _eventsPerPerson[str(vals['participantId'])] + [vals]
#             if "killerId" in str(vals) and "BUILDING_KILL" not in str(vals):
#                 _eventsPerPerson[str(vals['killerId'])] = _eventsPerPerson[str(vals['killerId'])] + [vals]
#     except KeyError:
#         continue
#         # print "skipped", str(items['participantFrames'])
#
# for items in _eventsPerPerson['5']:
#     print items
