#coding=utf-8
from sys import exit

def king_room():
    print "Please input the right number to save the king."

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        lose("The number is wrong.")

    if how_much == 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        lose(".............!")

def pet_room():
    print "There are some pets here."

    police_moved = False

    while True:
        next = raw_input("> ")

        if next == "Panda":
            lose("The Panda is national treasure.")
        elif next == "Dog" and not police_moved:
            print "The police has moved from the door. You can go through it now."
            police_moved = True
        elif next == "Dog" and police_moved:
            lose("The police found you.")
        elif next == "Tiger" and police_moved:
            king_room()
        else:
            print "I got no idea what that means."
            exit(0)

def fruit_room():
    print "Apple , Pear, or Bananas."
  

    next = raw_input("> ")

    if "Apple" in next:
        start()
    elif "Bananas" in next:
        lose("monkey kill you!")
    else:
        fruit_room()

def lose(why):
    print why, "Thank you for your participation!"
    exit(0)

def start():
    print "You need to access different rooms to find the King."
    print "There are two choices pet and fruit."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "pet":
        pet_room()
    elif next == "fruit":
        fruit_room()
    else:
        dead("You stumble around the room until you starve.")

start()
