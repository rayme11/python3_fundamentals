import random

def rollDice():
    totalSum = random.randint(1, 6) + random.randint(1, 6)
    return totalSum


player1 = input('Enter your name player 1\n')
roll1 = rollDice()

print('---------------------------------------')

player2 = input('Enter your name player 2\n')
roll2 = rollDice()

print('---------------------------------------')
print('Player 1 rolled: ' + str(roll1))

print('---------------------------------------')
print('Player 2 rolled: ' + str(roll2))
print('---------------------------------------')

if (roll1 > roll2):
    print('Player 1 wins')
elif (roll2 > roll1):
    print("Player 2 wins")
else:
    print('There must be a tie')



