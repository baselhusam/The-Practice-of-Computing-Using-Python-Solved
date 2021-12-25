#Exercise 40

import random

actions = ['rock','paper','scissors']

user = input("Enter a choice (rock, paper, scissors): ")
computer = random.choice(actions)

print("\nYou chose {}, and computer chose {}\n".format(user,computer))

if user == computer:
    print("Both players selected {}. It's a tie!".format(user))
elif user == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
        
        