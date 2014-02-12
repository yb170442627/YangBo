# -*- coding: utf-8 -*-

from sys import exit
from random import randint

def death():
    quips = ["You died. You kinda suck at this.",
             "Nice job, you died ...jackass.",
             "Such a luser.",
             "I have a small puppy that's better at this."]
    print quips[randint(0, len(quips)-1)]
    exit(1)
	
def first_method():
    print "escape pod."
    
    action = raw_input("> ")
	
    if action == "shoot!":
	    print "you are dead.Then he eats you."
	    return 'death'
		
    elif action == "dodge!":
	    print "your head and eats you."
	    return 'death'
		
    elif aciotn == "tell a joke":
	     print "putting him down."
	     return 'laser_weapon_armory'
		 
    else:
	     print "DOES NOT COMPUTE"
	     return 'central_corridor'
		 
def laser_weapon_armory():
    print "get the bomb. The code is 3 digits."
    code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
    guess = raw_input("[keypad]> ")
    guesses = 0