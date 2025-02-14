# import random

# # Choices available
# choices = ["rock", "paper", "scissors"]

# # User input
# user_choice = input("Enter rock, paper, or scissors: ").lower()

# # Computer's random choice
# computer_choice = choices[random.randint(0, 2)]

# print("Computer chose:", computer_choice)

# # Game logic
# if user_choice == computer_choice:
#     print("It's a tie!")
# elif (user_choice == "rock" and computer_choice == "scissors") or \
#      (user_choice == "paper" and computer_choice == "rock") or \
#      (user_choice == "scissors" and computer_choice == "paper"):
#     print("You win! 🎉")
# elif user_choice in choices:
#     print("Computer wins! 😢")
# else:
#     print("Invalid input. Please enter rock, paper, or scissors.")

import random

# Choices available
choices = ["rock", "paper", "scissors"]

# Score tracking
user_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors! Best of 5 rounds.\n")

# Best of 5 loop
while user_score < 3 and computer_score < 3:
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.\n")
        continue

    # Computer's random choice
    computer_choice = choices[random.randint(0, 2)]

    print("Computer chose:", computer_choice)

    # Game logic
    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        user_score += 1
        print("You win this round! 🎉\n")
    else:
        computer_score += 1
        print("Computer wins this round! 😢\n")

    print("Score - You:", user_score, "| Computer:", computer_score, "\n")

# Final result
if user_score == 3:
    print("Congratulations! You won the best of 5 series! 🏆")
else:
    print("Computer wins the best of 5 series! Better luck next time. 🤖")

