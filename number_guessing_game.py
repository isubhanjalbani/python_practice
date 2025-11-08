import random

def display_welcome_message():
    """Display welcome message and game instructions"""
    print("=" * 50)
    print("Welcome to the Number Guessing Game!")
    print("=" * 50)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    print("=" * 50)
    print()

def get_valid_guess():
    """Get and validate user input for their guess"""
    while True:
        try:
            guess = input("Enter your guess (1-100): ")
            guess_number = int(guess)
            
            # Check if the number is in valid range
            if guess_number < 1 or guess_number > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            return guess_number
            
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def play_game():
    """Main game logic"""
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    # Display welcome message
    display_welcome_message()
    
    # Game loop - continues until user guesses correctly
    while True:
        # Get valid guess from user
        guess = get_valid_guess()
        attempts += 1
        
        # Provide feedback based on the guess
        if guess < secret_number:
            print("Too low! Try again.")
            print()
        elif guess > secret_number:
            print("Too high! Try again.")
            print()
        else:
            # User guessed correctly
            print()
            print("=" * 50)
            print(f"🎉 Correct! You guessed the number!")
            print(f"The secret number was: {secret_number}")
            print(f"Number of attempts: {attempts}")
            print("=" * 50)
            break

def play_again():
    """Ask user if they want to play again"""
    while True:
        choice = input("\nWould you like to play again? (yes/no): ").lower()
        
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def main():
    """Main function to run the game"""
    print()
    
    # Game loop - allows multiple rounds
    while True:
        play_game()
        
        # Check if user wants to play again
        if not play_again():
            print("\nThank you for playing! Goodbye! 👋")
            break
        else:
            print("\n" + "=" * 50)
            print("Starting a new game...")
            print("=" * 50)
            print()

# Entry point of the program
if __name__ == "__main__":
    main()
