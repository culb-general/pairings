#A simple script for testing pypair

from pypair import Tournament
import random
import os
import sys
import json
import six
import operator

home = os.path.expanduser("~")

to = Tournament()

#for p in range(10):
#    to.addPlayer( p, "Timmy" )

#to.loadPlayersCSV("/home/lemon/pairings/swiss/pypair/playerlist.csv")
#to.loadPlayersCSV(sys.argv[1])
players_cnt = int(sys.argv[1])
cnt = int(sys.argv[2])

# def addPlayer( self, IDNumber, playerName, fixedSeating=False ):
for i in range(players_cnt):
    to.addPlayer(str(i+1), "Player%s" % str(i+1), False)

for i in range(cnt):
    pairings1 = to.pairRound()
    print(pairings1)

    for table in pairings1:
        if not type(pairings1[table]) is str:
            #print(pairings1[table])
            pts = random.randint(0,20)
            to.reportMatch(table, [pts, 20-pts, 0])
            print("%s vs %s -- %s:%s" % (pairings1[table][0], pairings1[table][1], pts, 20-pts))
    to.saveEventData("%s/datadump%s.txt"%(home,i))
    print("")
#print to.playersDict[256]
    print("")
#print(json.dumps(to.dumpTournamentData()))

#tournament_table = list(to.playersDict.items()).sort(key=operator.itemgetter('Points'))
player_arr = []
for key, val in six.iteritems(to.playersDict):
    player_arr.append(val)
#tournament_table = player_arr.sort(key=operator.itemgetter('Points'))

for player in sorted(player_arr, key=operator.itemgetter('Points'), reverse=True):
	print("%s: %s" % (player['Name'], player['Points']))

#print("")
#print(to.playersDict[1])
#print("")
