name = input("Type your name:")
print("Welcome", name, "to the adventure")

answer = input("YOU ARE ON A DIRT ROAD THAT HAS COME TO AN END DO YOU  WANT TO GO LEFT OR RIGHT?").lower()

if answer == "left":
    answer = input("You find a castle, will you enter the castle or will you walk past? WALK IN / WALK PAST").lower()
    if answer == "walk in":
        print("A trap in the castle kills you")
    if answer == "walk past":
        print("While walking around a wild animal hunts and kills you")
elif answer == "right":
    answer = input("You come across a bridge, do you cross or go back?. CROSS/ GO BACK").lower()
    if answer == "cross":
        answer = input("You cross the bridge and meet a strange man. TALK / IGNORE").lower()
        if answer == "talk":
            print("The stranger tells you to wake up and you wake up, it was all a dream. YOU WIN!")
        if answer == "ignore":
            print("The stranger curses you and you never wake up. YOU LOSE")
    if answer == "go back":
        print("While walking back, a wild animal hunts and kills you")

else:
    print("you lose")

print("Thank you for playing", name)