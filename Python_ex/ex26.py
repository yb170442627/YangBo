# -*- coding: utf-8 -*-
#import ex25.py  ImportError: No module named py
import ex25
#from ex25 import *

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): #def语句要以 “冒号” 结尾
    """Prints the first word after popping it off."""
    #word = words.poop(0) AttributeError: 'list' object has no attribute 'poop'
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) #左右括号是成对出现的
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 #注意反斜杠和除号的区别
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
#beans, jars, crates == secret_formula(start-point)
beans, jars, crates = secret_formula(start_point)
print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
#print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont) 
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)

sentence = "All god\tthings come to those who weight."

words = ex25.break_words(sentence) #此处需要引用到ex25.py里面的方法，所以需要在开头的时候把ex25.py里面的函数导入
sorted_words = ex25.sort_words(words)#导入方式为：import ex25

print_first_word(words)
print_last_word(words)
#.print_first_word(sorted_words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
#prin sorted_words
print sorted_words

#print_irst_and_last(sentence) NameError: name 'print_irst_and_last' is not defined
print_first_and_last(sentence)

   #print_first_a_last_sorted(senence)

#print_first_a_last_sorted(senence)NameError: name 'print_first_a_last_sorted' is not defined

#print_first_and_last_sorted(senence) NameError: name 'senence' is not defined
print_first_and_last_sorted(sentence)

'''
The output is as follows:

PS F:\Python_ex> python .\ex26.py
Let's practice everything.
You'd need to know 'bout escapes with \ that do
 newlines and    tabs.
--------------

        The lovely world
with logic so firmly planted
cannot discern
 the needs of love
nor comprehend passion from intuition
and requires an explantion

                where there is none.

--------------
This should be five: 6
With a starting point of: 10000
We'd have 5000000 jeans, 5000 jars, and 50 crates.
We can also do that this way:
We'd have 500000 beans, 500 jars, and 5 crabapples.
All
weight.
All
who
['All', 'come', 'god\tthings', 'those', 'to', 'weight.', 'who']
All
weight.
All
who

'''