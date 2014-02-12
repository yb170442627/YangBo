# -*- coding: utf-8 -*-

#this one is like your scripts with argv
def print_two(*args):#*号的作用： 它的功能是告诉 python 让它把函数的所有参数都接受进来，然后放到名字叫 args 的列表中去。
 arg1, arg2 = args
 print "arg1: %r, arg2: %r" % (arg1,arg2)

'''
def print_two(*args):
    arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	IndentationError: unexpected indent 
	(此段代码运行的时候会报这个错误，这是一个代码格式的错误),此处容易犯一个错误，在写完第二行后，直接回车了。
	这样就导致了print的上一层不是def，而是代码的第二行。正确写法，参考4-7行。
'''
#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2): #def 是用来创建一个函数，用 "："结束，如果此处缺少冒号，讲会报错“SyntaxError: invalid syntax”
    print "arg1:%r, arg2: %r" % (arg1,arg2)
	
#this just take on argument
def print_one(arg1):
    print "arg1: %r" % (arg1)
	
#this one takes no argument
def print_none():
    print "I got nothing."
	
print_two("Felix","Yang")
print_two_again("Felix","Yang")
print_one("First!")
print_none()

'''
The output is as follows:
PS G:\Python_ex> python .\ex18.py
arg1: 'Felix', arg2: 'Yang'
arg1:'Felix', arg2: 'Yang'
arg1: 'First!'
I got nothing.

'''


