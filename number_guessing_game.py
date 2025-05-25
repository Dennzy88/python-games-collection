import random

number_to_guess = random.randint(1, 100)
while True:
    try:
        
        guess = int(input("Guess the number (between 1 and 100): "))

        
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Well done! You guessed the number.")
            break
    # Handle invalid input
    except ValueError:
     print("Invalid input. Please enter a number.")
    
    