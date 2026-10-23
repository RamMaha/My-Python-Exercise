import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "<== User Wins! ==>"
    else:
        return "<== Computer Wins! ==>"

def main():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        print("\nChoose an option:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        
        choice = input("Enter your choice: ")
        if choice not in ["1", "2", "3"]:
            print("Invalid choice, try again.")
            continue

        user_choice = {"1": "Rock", "2": "Paper", "3": "Scissors"}[choice]
        computer_choice = get_computer_choice()

        print(f"\nUser choice is: {user_choice}")
        print("Now it's Computer's Turn...")
        print(f"Computer choice is: {computer_choice}")
        print(f"{user_choice} vs {computer_choice}")
        print(decide_winner(user_choice, computer_choice))

        play_again = input("\nDo you want to play again? (Y/N): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
