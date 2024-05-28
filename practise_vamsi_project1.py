import random

# get a random number between 1 and 6 (including 1 and 6) rolling a dice
def roll():
    min_value=1
    max_value=6
    roll = random.randint(min_value,max_value)
    return roll

number = roll()

# get a valid number of players between 2 and 4
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")




range(players)

# play the game
max_score = 50
players_scores = []
