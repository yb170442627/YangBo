# -*- coding: utf-8 -*-

cars = 1000
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are" , cars , "cars available."
print "There are only", drivers , "drivers available."
print "There will be", cars_not_driven , "empty cars today."
print "We can transport" , carpool_capacity, "people today"
print "We have", passengers , "to carpool today."
print "We need to put about", average_passengers_per_car, "people in each car."

'''
The output is as follows:

There are 1000 cars available.
There are only 30 drivers available.
There will be 970 empty cars today.
We can transport 120 people today
We have 90 to carpool today.
We need to put about 3 people in each car.
'''