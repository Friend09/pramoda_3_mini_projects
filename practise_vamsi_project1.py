import random


def roll():
    min_value=1
    max_value=6
    roll = random.randint(min_value,max_value)
    print(roll)
    return roll

number = roll()
print(number)
