import random

biggest_num =  input("Type a number:")

if biggest_num.isdigit():
    biggest_num = int(biggest_num)

    if biggest_num < 0:
            print("input a num bugger than 0")
else:
    print("input an integer")

rand_num = random.randint(0, biggest_num)

guesses = 0

while True:
    guess = input("Guess the number: ")
    guesses += 1

    if guess.isdigit():

        guess = int(guess)

    else:
        print("input an integer")
        continue

    if guess == rand_num:
        print("you guessed the correct num")
        break
    elif guess > rand_num:
        print("guess lower")
    else:
        print("guess higher")

print("It took you", guesses, "guesses")

