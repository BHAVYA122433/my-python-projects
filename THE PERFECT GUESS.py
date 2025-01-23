import random

n = random.randint(0, 100)
print('You are in a game')
user_guess = None
i = 1

while user_guess != n:
    user_guess = int(input('Please enter your guess --> '))
    
    if user_guess > n:
        print('Enter a lower number')
        i += 1
        
    elif user_guess < n:
        print('Enter a higher number')
        i += 1
    
    else: 
        print('You guessed right!')
        print(f'You took a total of {i} guesses')

