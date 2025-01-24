# NOTE--> THIS CODE IS BEING IMPROVED BY DEEPSEEK TO INCREASE IT'S ACCURACY!!

import random

def generate_question():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # Choose a random operation: +, -, or *
    operation = random.choice(['+', '-', '*'])
    
    # Calculate the correct answer
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    
    # Return the question and the correct answer
    return f"What is {num1} {operation} {num2}?", correct_answer

def math_quiz():
    score = 0
    num_questions = 5  # Number of questions to ask
    
    print("Welcome to the Math Quiz!")
    print(f"You will be asked {num_questions} questions. For each correct answer, you get +4 points. For each wrong answer, you lose -1 point.\n")
    
    for i in range(num_questions):
        question, correct_answer = generate_question()
        print(f"Question {i+1}: {question}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            user_answer = None
        
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 4
        else:
            print(f"Wrong! The correct answer is {correct_answer}.\n")
            score -= 1
    
    print(f"Quiz over! Your final score is: {score}")

# Run the quiz
math_quiz()
