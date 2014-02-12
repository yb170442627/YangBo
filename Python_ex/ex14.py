# -*- coding: utf-8 -*-

from sys import argv

script, user_name ,user_id = argv
prompt = '> '

print "Hi %s, I'm the %s script.You id is %s" %(user_name, script, user_id)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "Do you want to change your id to?" %user_id
ID = raw_input(prompt)

print """
Alright , so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. 
And you want to have a new id %r.
Nice.
""" % (likes,lives,computer,ID)

'''
The output is as follows:

Hi YangBo, I'm the .\ex14.py script.You id is 9527
I'd like to ask you a few questions.
Do you like me YangBo?
> Y
Where do you live YangBo
> SH
What kind of computer do you have?
> APPLE
Do you want to change your id to 9527?
> 1314

Alright , so you said 'Y' about liking me.
You live in 'SH'. Not sure where that is.
And you have a 'APPLE' computer.
And you want to have a new id '1314'.
Nice.

'''
