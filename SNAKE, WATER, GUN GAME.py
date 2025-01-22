import random

# 0 <--> snake, 1 <--> water, 2 <--> gun

computer_choice = random.choice([0, 1, 2])
user_input = input('Please choose one of the following options: snake, water, or gun --> ').lower()

choices_dict = {"snake": 0, "water": 1, "gun": 2}
reverse_dict = {0: 'snake', 1: 'water', 2: 'gun'}

user_choice = choices_dict.get(user_input)

if user_choice is None:
    print("Invalid choice. Please choose from snake, water, gun.")
else:
    print(f'Computer chose {reverse_dict[computer_choice]}')
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 1) or \
         (user_choice == 1 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 0):
        print("You won!")
    else:
        print("You lost.")
