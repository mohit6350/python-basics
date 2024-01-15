# Write a Python program that generates a random number between 1 and 10 and asks the user to guess the number. The program should continue to prompt the user for guesses until they correctly guess the number. After each incorrect guess, the program should provide a hint to the user if the correct number is higher or lower than their guess.

import random

def guess_the_number():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Initialize variables
    guessed_number = 0
    attempts = 0

    print("Welcome to the Guess the Number Game! You have three attempts")
    
    while attempts < 3:
        guessed_number = int(input("Enter number : "))
        attempts += 1
        
        if guessed_number == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            return
    
    print("Sorry! No more attempts left")    
         
    

# Call the function to play the game

if __name__ == "__main__":
    guess_the_number()
