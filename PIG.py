#player rolls a dice until they hit 50, but if you roll a one you reset

import random

def roll():
    min_value =  1 
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll #who ever calls the function can see the value



while True:
    players = input("How many players? (max 4)")
    if players.isdigit():
        players = int(players)
        if players >= 2 and players <= 4: 
            break
        else:
            print("Insert a valid amount of players")
    else:
        print("Invalid")

max_score = 50
player_scores = 