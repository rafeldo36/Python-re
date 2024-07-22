import random

def get_computer_choice():
    choices = ['snake', 'water', 'gun']
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'snake' and computer == 'water') or \
         (player == 'water' and computer == 'gun') or \
         (player == 'gun' and computer == 'snake'):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Welcome to Snake, Water, Gun!")
    player_choice = input("Enter your choice (snake, water, gun): ").lower()
    
    while player_choice not in ['snake', 'water', 'gun']:
        print("Invalid choice! Please choose again.")
        player_choice = input("Enter your choice (snake, water, gun): ").lower()
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
