import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    if result == 'tie':
        print("It's a tie! 🟡")
    elif result == 'win':
        print("Congratulations! You win! 🟢")
    else:
        print("Oops! You lose 🔴")

def print_instructions():
    print("Welcome to Rock, Paper, Scissors!")
    print("Here's how to play:")
    print("1. Type 'rock', 'paper', or 'scissors'.")
    print("2. The computer will make its choice.")
    print("3. The winner is determined based on the rules:")
    print("   - Rock beats Scissors")
    print("   - Scissors beat Paper")
    print("   - Paper beats Rock")
    print("4. Scores will be displayed after each round.")
    print("5. You can choose to play again or exit the game.")

def play_game():
    user_score = 0
    computer_score = 0

    print_instructions()
    
    while True:
        user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, result)

        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1
        
        print(f"\nCurrent Score: You {user_score} - {computer_score} Computer")
        
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nThank you for playing! Final Score:")
    print(f"You {user_score} - {computer_score} Computer")
    print("Goodbye! Have a great day!")

if __name__ == "__main__":
    play_game()
