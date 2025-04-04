# NUIST Quiz Game in Python
# Auther: Yang Yue
# Student NUIST ID: 202283890018
# Student SETU ID: W20109667

#Define a function named quiz to execute the Q&A game.
def quiz():
    # Print a welcome message.
    print("Welcome to  the Animal Quiz!")
    # Print a prompt message.
    print("Answer the following questions:")


# Questions and Answers
    # Define a list containing multiple questions.
    questions = [
        "1. What is the largest animal on Earth?: a. Blue Whale, b. Mouse, c. Cat\n",
        "2. Which bird can fly backwards?: a. Cuckoo, b. Eagle, c. Hummingbird\n",
        "3. What is the only mammal capable of flight?: a. Bat, b. Squirrel, c. Dolphin\n"
    ]

    # Define a list containing the correct answers.
    answers = [
        "a", 
        "c", 
        "a"
    ]
    # Initialize the user's score with an initial value of 0.
    score = 0


#Ask questions
    # Use a for loop to iterate through each question in the questions list.
    for i in range(len(questions)):
        # Prompt the user to enter an answer.
        user_answer = input(questions[i]).strip().lower()
        # Check if the user's input answer matches the correct answer.
        if user_answer == answers[i]:
            # Print a prompt message when the answer is correct.
            print("Correct!")
            # Increase the score by 1.
            score += 1
        else:
            # Print a prompt message when the answer is incorrect.
            print("Incorrect!")


# Provide final score
    # Print a prompt message indicating the end of the Q&A game.
    print("\nQuiz completed!")
    # Print the user's final score.
    print(f"You got {score}/{len(questions)} questions correct.")

# Run the quiz function
quiz()
