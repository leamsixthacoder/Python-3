import random

choices = random.choice(['rock', 'paper', 'scissors'])

user_choice = input('Enter your choice: ')

print(f'Computer choice: {choices}')

if user_choice == choices:
    print('It\'s a tie!')
elif user_choice == 'rock' and choices == 'scissors':
    print('You win!')
elif user_choice == 'paper' and choices == 'rock':
    print('You win!')
elif user_choice == 'scissors' and choices == 'paper':
    print('You win!')
else:
    print('You lose!')


