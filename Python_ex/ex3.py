# -*- coding: utf-8 -*-


# + plus [plʌs]
# - minus ['maɪnəs]
# / slash [slæʃ]
# * asterisk ['æstərɪsk]
# % percent [pə'sent]
# < less-than
# > greater-than
# < = less-than-equal
# > = greater-than-equal

print "I will now count my chickens:"

print "Hens" , 25 + 30 / 6 # 25 + 5 = 30
#浮点数
print "Hens" , round (25.0 + 30 / 7.0 ) # 使用round()函数给浮点数取整

print "Roosters" , 100 - 25 * 3 % 4 # (25*3=75 , 75 % 4 = 3 , 100 -3 =97) 97

print "Now I will count the eggs:"

print 3 + 2 + 1 -5 +4 % 2 - 1 / 4 + 6 # 7

print 3 + 2 + 1 -5 +4 % 2 - 1 / 4.0 + 6 #6.75

print "Is it true that 3 + 2 < 5 - 7 ?"

print 3 + 2 < 5 - 7 # False

print "What is 3 + 2?" , 3 + 2 # 5
print "What is 5 - 7?" , 5 - 7 # -2

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?" , 5 > -2 # True
print "Is it greater or equal?" , 5 >= -2 # True
print "Is it less or equal?", 5 <= -2 # False

'''
The output is as follows:

I will now count my chickens:
Hens 30
Hens 29.0
Roosters 97
Now I will count the eggs:
7
6.75
Is it true that 3 + 2 < 5 - 7 ?
False
What is 3 + 2? 5
What is 5 - 7? -2
Oh, that's why it's False.
How about some more.
Is it greater? True
Is it greater or equal? True
Is it less or equal? False
'''