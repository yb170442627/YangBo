# -*- coding: utf-8 -*-

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # '%r' 是为了格式化后面的变量‘hilarious’。如果此处把'%r'去掉，则下面那条语句执行时会报错
                                                         #TypeError: not all arguments converted during string formatting
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e


'''
The output is as follows:

There are 10 types of people.
Those who know binary and those who don't.
I said: 'There are 10 types of people.'.
I also said: 'Those who know binary and those who don't.'.
Isn't that joke so funny?! False
This is the left side of...a string with a right side.
'''