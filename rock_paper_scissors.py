import random

user_w = 0
comp_w = 0

options = ["rock", 'paper', 'scissors']

while True:
    user_input = input("Rock/Paper/Scissors, Q to Quit ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    rand_number = random.randint(0, 2)
    # 0 = rock, 1 = paper, 2  = scissors
    comp_input = options[rand_number]
    print("Computer picked ", comp_input)

    if user_input == "rock" and comp_input == "scissors":
        print("You Won")
        user_w += 1
    elif user_input == "paper" and comp_input == "rock":
        print("You Won")
        user_w += 1
    elif user_input == "scissors" and comp_input == "paper":
        print("You Won")
        user_w += 1
    elif user_input == comp_input:
        print("its a tie, no points given")
    else:
        print("You lost")
        comp_w += 1


print("Game Ended")
print("You have ", user_w, " wins, the computer has ", comp_w, " wins")