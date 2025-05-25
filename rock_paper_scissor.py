import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"
emojis = {
    ROCK: "✊",
    PAPER: "✋",
    SCISSORS: "✌️"
}
choices = tuple(emojis.keys())
# Rock, Paper, Scissors Game

def get_user_choice():
    while True:
        user_choice = input("Rock, paper, scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please enter 'r', 'p', or 's'.")

def display_choices(user_choice, computer_choice):
    print(f"You chose: {user_choice} {emojis[user_choice]}")
    print(f"Computer chose: {computer_choice} {emojis[computer_choice]}")           
 
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
            print("It's a tie!")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or \
        (user_choice == PAPER and computer_choice == ROCK) or \
        (user_choice == SCISSORS and computer_choice == PAPER)):
        print("You win!")
    else:
        print("You lose!")  
        
def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'n':
            print("Thank you for playing!")
            break
        elif play_again == 'y':
            print("Great! Let's play again!")
play_game()
