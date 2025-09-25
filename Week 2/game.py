import random
options = ["rock", "paper", "scissors"]
player_choice = input("Enter rock, paper, or scissors: ")
computer_choice = random.choice(options)
print(f"\nyou chose: {player_choice}")
print(f"Computer chose: {computer_choice}")

if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or\
     (player_choice == "paper" and computer_choice == "rock") or\
     (player_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("computer wins!")
