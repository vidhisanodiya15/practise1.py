from multiprocessing import parent_process
import random


user_input = input("Enter a choice : Rock ,paper, scissors")
possible_action = ["rock","paper","scissors"]
computer_action = random_choice ("possible action")
if user_input == computer_action:
    print("Tie")
elif user_input== "Rock":
    if computer_action == "paper":
        print("You lose")
    else:
        print("You win")
elif user_input=="Paper":
    if computer_action== "Scissors":
     print("You lose")
else:
    print("You win")
elif user_input== 



