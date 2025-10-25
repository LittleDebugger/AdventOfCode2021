# Common template
# import math
# import numpy as np
import re
# from collections import defaultdict as dd
from collections import Counter

# file = [re.split(' |=|by|x', line.strip()) for line in file]

# standard
file = [line.strip() for line in open("input.txt")]

# split single line by comma
# file = [int(a) for a in re.split(',', list(open("input.txt"))[0])]

# split each line by x
# file = [[int(a) for a in re.split('x', line.strip())] for line in open("input.txt") ]

print(file)

playerPlace = dict()
playerScore = dict()

dice = 1

for line in file:
    s = re.split(' |:', line)
    print(s)
    playerPlace[int(s[1])] = int(s[5])
    playerScore[int(s[1])] = 0

turn = 1
y = 0

winScore = 21

games = dict()


# (player1 position, player1 score, position, player 2 play 2 score, turn)

def calc(place, score, roll):
    place = (place + roll - 1)
    place = (place % 10) + 1
    return (place, score + place)

def getNext(game, count, nextGames):
    global possibles
    player1Place = game[0]
    player1Score = game[1]
    player2Place = game[2]
    player2Score = game[3]
    turn = game[4]
    if turn == 1:
        for pos in possibles:
            next = calc(player1Place, player1Score, pos[0])
            game = (next[0], next[1], player2Place, player2Score, 2)
            if game in nextGames:
                nextGames[game] += (count * pos[1])
            else:
                nextGames[game] = (count * pos[1])
    else:
        for pos in possibles:
            next = calc(player2Place, player2Score, pos[0])
            game = (player1Place, player1Score, next[0], next[1], 1)
            if game in nextGames:
                nextGames[game] += (count * pos[1])
            else:
                nextGames[game] = (count * pos[1])

games[(playerPlace[1], playerScore[1], playerPlace[2], playerScore[2], turn)] = 1

possibles = []
for i in range(3):
    for ii in range(3):
        for iii in range(3):
            possibles.append(i + ii + iii + 3)
possibles = Counter(possibles).most_common()
possibles.reverse()

# add the games

print(games)

player1Wins = 0
player2Wins = 0

while len(games) > 0:
    y += 1
    nextGames = dict()
    for game in games:
        count = games[game]
        #print('count = ', count)
        getNext(game, count, nextGames)
    games = nextGames
    #print(nextGames)
    #if y > 1:
     #   exit()
    removals = []
    for game in games:
        if game[1] >= winScore:
            player1Wins += games[game]
            removals.append(game)
        if game[3] >= winScore:
            player2Wins += games[game]
            removals.append(game)
    for removal in removals:
        games.pop(removal)


print(player1Wins)
print(player2Wins)