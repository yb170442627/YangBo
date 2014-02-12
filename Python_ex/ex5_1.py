# -*- coding: utf-8 -*-

name = 'YangBo'
age = 35 # not a lie
height = 74 # inches : 英寸
weight = 180 # lbs (pounds) 磅
eyes = 'Bule'
teeth = 'White'
hair = 'Brown'

#%s,表示格化式一个对象为字符， 把 name代表的字符串放到%s的位置中
print "Let's talk about %s." % name
#%d,整数. 把 height 代表的整数放到 %d 的位置中
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
#%r : 不管什么都打印出来 ， 所以这边的打印出来的name是 ‘YangBo’


print " %r He's got %s eyes and %s hair" % (name,eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d , %d and %d I get %d." %(
   age, height, weight, age + height + weight)
   
   
'''
The output is as follows:
Let's talk about YangBo.
He's 74 inches tall.
He's 180 pounds heavy.
Actually that's not too heavy.
 'YangBo' He's got Bule eyes and Brown hair
His teeth are usually White depending on the coffee.
If I add 35 , 74 and 180 I get 289.

'''