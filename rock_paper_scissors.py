import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type (rock, paper, scissors) or q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Please type a valid input")
        continue
    random_number = random.randint(0, 2)
    # 0 = rock, 1 = paper, 2 = scissors
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1
    
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")