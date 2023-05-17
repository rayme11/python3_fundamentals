import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])

user_choice = str(input('Do you want rock, paper, scissors?\n'))
print('Machine is chosing ' + computer_choice)

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('YOU BEAT THE MACHINE because ' + user_choice + ' beats ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print('YOU BEAT THE MACHINE because ' + user_choice + ' beats ' + computer_choice)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('YOU BEAT THE MACHINE because ' + user_choice + ' beats ' + computer_choice)
else:
    print('The machine beat you' + ' because it chose: ' + computer_choice + ' and you chose ' + user_choice)

