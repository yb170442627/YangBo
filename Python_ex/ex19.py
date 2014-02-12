# -*- coding: utf-8 -*-

def cheese_and_crackers (cheese_count , boxes_of_crackers):
    print "You have %s cheeses" % cheese_count #cheeses(奶酪)
    print "You have %d boxes of crackers!" % boxes_of_crackers #crackers(咸饼干)
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
	
print "We can just give the function number directly:"
#NameError: name 'cheese_and_carckers' is not defined
#cheese_and_carckers(20, 30)  函数名称要保持一致
cheese_and_crackers(20*3, 30-5)


print "OR, we can use variables from our scripts:" #variables(变量)
amount_of_cheese = 10 
amount_of_crackers = 50 + amount_of_cheese
amount_of_crackers = 100 

'''
允许出现相同的变量名称，后面这个变量的值替换了前面那个同名变量的值
也就是说，程序在执行的时候，调用的是100这个值，而不是60
'''

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers("10+20", 5+19)

print "And we can combine the two, variables and math:" #combine(混合，联合)
cheese_and_crackers(amount_of_cheese + 32, amount_of_crackers+17)

'''
The output is as follows:

PS G:\Python_ex> python .\ex19.py
We can just give the function number directly:
You have 60 cheeses
You have 25 boxes of crackers!
Man that's enough for a party!
Get a blanket.

OR, we can use variables from our scripts:
You have 10 cheeses
You have 60 boxes of crackers!
Man that's enough for a party!
Get a blanket.

We can even do math inside too:
You have 30 cheeses
You have 24 boxes of crackers!
Man that's enough for a party!
Get a blanket.

And we can combine the two, variables and math:
You have 42 cheeses
You have 77 boxes of crackers!
Man that's enough for a party!
Get a blanket.
'''


