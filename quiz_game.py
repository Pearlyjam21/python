print("Welcome to my quiz")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Lets play")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct :3")
    score += 1
else:
    print("Wrong!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("correct :3")
    score += 1
else:
    print("Wrong!")

print("You got " + str(score) + " questions correct")
print("You got " + str((score / 2) * 100) + "%")


