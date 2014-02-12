# -*- coding: utf-8 -*-

class TheThing(object):

    def __init__(self):
	  self.number = 0
	  
    def some_function(self):
	   print "I got called."
	   
    def add_me_up(self,more):
      self.number += more
      return self.number  		
		
# two different things
a = TheThing() #将类赋值给一个变量
b = TheThing()		

a.some_function()
b.some_function()

print a.add_me_up(20) # 将20,30传递给函数add_more_up(self, more)中的more
print b.add_me_up(30)

print a.number 
print b.number

# Study this. This is how you pass a variable
# from one class to another. You will need this.
class TheMultiplier(object):

    def __init__(self,base):
	  self.base = base
	
    def do_it(self, m):
	  return m * self.base

x = TheMultiplier(a.number) # x = 20
print x.do_it(b.number) # 20 *30 = 600

