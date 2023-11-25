import random

options = ("rock", "paper", "scissors")

def playerchoice():
    while True:
        player = input("Enter a choice (rock, paper, scissors): ").lower()
        if player in options:
            return player
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

def playgame():
    while True:
        player = playerchoice()
        computer = random.choice(options)
        print(f"Computer: {computer}")
        print(winner(player, computer))
        if input("Play again? (y/n): ").lower() != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    playgame()
