#A simple script for testing pypair

from pypair import Tournament
import random
import os
import sys
import json
import six
import operator

home = os.path.expanduser("~")
import cProfile
to = Tournament()



#for p in range(10):
#    to.addPlayer( p, "Timmy" )

#to.loadPlayersCSV("/home/lemon/pairings/swiss/pypair/playerlist.csv")
#to.loadPlayersCSV(sys.argv[1])

Clubs = ["General", "OBTU", "Onion", "La Frontier"]
Armies = ["Vanilla", "BA", "Necrons", "Eldars", "SoB", "Tau"]
Towns = ["Moscow", "Moscow", "Moscow", "Moscow", "Moscow", "Moscow", "SPb", "SPb", "Kaluga", "Novosibirsk", "Yekaterinburg", "Tver", "Tula", "Voronezh"]

def test_pairings():
    players_cnt = int(sys.argv[1])
    cnt = int(sys.argv[2])
    hysteresis = 2
    if len(sys.argv) >= 4:
        hysteresis = int(sys.argv[3])
    to.hysteresis = hysteresis
    # def addPlayer( self, IDNumber, playerName, fixedSeating=False ):
    for i in range(players_cnt):
        to.addPlayer(str(i+1), "Player%s" % str(i+1), False, Clubs[i % len(Clubs)], Armies[i % len(Armies)], Towns[i % len(Towns)])

    for i in range(cnt):
        #print("==========\nRound %s\n==========" % str(i + 1))
        #pairings1 = 
        pairings1 = to.pairRound()

        for table in pairings1:
            if not type(pairings1[table]) is str:
                #print(pairings1[table])
                pts = random.randint(0,20)
                to.reportMatch(table, [pts, 20-pts, 0])
                print("%s (%s from %s@%s) vs %s (%s from %s@%s) on table %s -- %s:%s" % (pairings1[table][0], to.playersDict[pairings1[table][0]]['army'], to.playersDict[pairings1[table][0]]['club'], to.playersDict[pairings1[table][0]]['town'], pairings1[table][1], to.playersDict[pairings1[table][1]]['army'], to.playersDict[pairings1[table][1]]['club'], to.playersDict[pairings1[table][1]]['town'], table, pts, 20-pts))
        if to.byePlayer != None:
            print("Player %s got the bye and %s points" % (to.byePlayer, to.byePoints))
        to.saveEventData("%s/datadump%s.txt"%(home,i))
        player_arr = []
        for key, val in six.iteritems(to.playersDict):
            player_arr.append(val)
        for player in sorted(player_arr, key=operator.itemgetter('Points'), reverse=True):
            print("%s (%s from %s@%s): %s" % (player['Name'], player["army"], player["club"], player["town"], player['Points']))
        print('')

#import cProfile
#cProfile.run('test_pairings()')
test_pairings()


#print("")
#print(to.dumpTournamentData())
#print("")
