import re
from collections import Counter

file = [line.strip() for line in open("input.txt")]

playerPlace = dict()
playerScore = dict()

dice = 1

for line in file:
    s = re.split(' |:', line)
    print(s)
    playerPlace[int(s[1])] = int(s[5])
    playerScore[int(s[1])] = 0

turn = 1
rolls = 0
y = 0

winScore = 21

games = dict()


# (player1 position, player1 score, position, player 2 play 2 score, turn)

def calc(place, score, roll):
    place = (place + roll - 1)
    place = (place % 10) + 1
    return (place, score + place)

def getNext(game, count):
    global games, possibles
    player1Place = game[0]
    player1Score = game[1]
    player2Place = game[2]
    player2Score = game[3]
    turn = game[4]
    for pos in possibles:


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
for game in games:
    count = games[game]
    games[game] = 0
    print(game, count)

    # count the wins and revmove then