# -*- coding: utf-8 -*-

people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."
	
elif cars > people and buses < cars:
    print "We should not take the cars."
	
else:
    print "We can't decide."
	
if buses > cars:
    print "That's too many buses."
	
elif buses < cars:
    print "Maybe we could take the buses."
	
else:
    print "We still can't decide."
	
if people > buses:
  print "Alright, let's just take the buses."
  
else:
    print "Fine, let's stay home then."
	

'''
The output is as follows:

PS F:\Python_ex> python .\ex30.py
We should take the cars.
Maybe we could take the buses.
Alright, let's just take the buses.

'''
'''
elif是python提供的else-if语句，它检查多个条件表达式的值是否为真，并在为真时执行特定代码块中的代码。
和else一样，elif是可选的，但是要注意的是，一个if语句可以跟多个elif语句，但最后只能有一个else语句：
'''