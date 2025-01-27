def adventure_game():
    print("Welcome to the Adventure Path Game!")
    print("Your goal is to survive the journey.")
    print("You will be given two options at each step. Choose wisely!")

    # Starting point
    choice1 = input("You are at the entrance of a dark forest. Do you want to go left or right? (left/right): ").lower()
    
    if choice1 == "left":
        choice2 = input("You encounter a wild animal. Do you want to fight or run? (fight/run): ").lower()
        
        if choice2 == "fight":
            print("You bravely fight the animal but unfortunately lose the battle. You lose!")
        elif choice2 == "run":
            print("You run away safely. You survive!")
        else:
            print("Invalid choice. You lose!")
    
    elif choice1 == "right":
        choice2 = input("You find a river. Do you want to swim across or build a raft? (swim/raft): ").lower()
        
        if choice2 == "swim":
            print("You try to swim across the river, but the current is too strong. You lose!")
        elif choice2 == "raft":
            print("You build a raft and float across the river. You survive!")
        else:
            print("Invalid choice. You lose!")
    
    else:
        print("Invalid choice. You lose!")

# Start the game
adventure_game()
