# -*- coding: utf-8 -*-

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    c = a + b
    print "%s" % c
    return c
	
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
	
def multiply(a ,b):
    print "MUTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" %(a, b)
    return a / b
	
print "Let's do some math with just functions!"

age = add(40 ,4)
height = subtract(54, 30)
weight = multiply(21, 98)
iq = divide(20, 5)

print "Age: %d, Height: %d, Weight: %d, IQ:%d" % (age, height, weight, iq)

#A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height,multiply(weight, divide(iq, 2))))

print "That becomes: ",what, "Can you do it by hand?"