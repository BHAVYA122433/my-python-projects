def ask_question(question, correct_answer):
    user_answer = input(question)
    if user_answer.lower() == correct_answer.lower():
        print('Correct!')
        return 1
    else:
        print(f"sorry your answer is incorrect, the correct answer was {correct_answer}")
        return 0

print("Welcome to my math quiz!")

if input("do you want to play? ").lower() not in ["yes", "yup", "yep", "ya", "certainly", "absolutely", "of course", "ofc","definitely", "sure", "for sure", "affirmative", "indeed", "uh-huh"]:
    quit()

print("okay! let's play :)")
score = 0

score += ask_question("What is 5 + 7? ", "12")
score += ask_question("What is 9 x 3? ", "27")
score += ask_question("What is the square root of 64? ", "8")
score += ask_question("What is 15 - 4? ", "11")

print(f"you got {score} questions correct!")
