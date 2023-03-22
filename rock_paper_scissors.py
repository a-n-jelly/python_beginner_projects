import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True: 
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        print("Try again")
        continue

    random_num = random.randint(0,2) # rock: 0, paper: 1, scissors: 2
    computer_guess = options[random_num]

    print("computer guessed", computer_guess + ".")

    if user_input == "rock" and computer_guess == "scissors":
        print("you win")
        user_wins += 1

    elif user_input == "paper" and computer_guess == "rock":
        print("you win")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_guess == "paper":
        print("you win")
        user_wins += 1

    else: 
        print("You lost")
        computer_wins += 1

print("Your score: ", user_wins, ", Computer Score: ", computer_wins)
print("Bye!")