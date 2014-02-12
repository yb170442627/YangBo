# -*- coding: utf-8 -*-

my_name = 'YangBo'
my_age = 35 # not a lie
my_height = 74 # inches : 英寸
my_weight = 180 # lbs (pounds) 磅
my_eyes = 'Bule'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d , %d and %d I get %d." %(
   my_age, my_height, my_weight, my_age + my_height + my_weight)
   
   
'''   
The output is as follows:
Let's talk about YangBo.
He's 74 inches tall.
He's 180 pounds heavy.
Actually that's not too heavy.
He's got Bule eyes and Brown hair
His teeth are usually White depending on the coffee.
If I add 35 , 74 and 180 I get 289.
'''