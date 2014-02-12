# -*- coding: utf-8 -*-
#程序目的
#接收用户输入的信息，并按照用户输入的值进行运算并打印
def cheese_and_crackers (cheese_count , boxes_of_crackers):
    print "You have %d cheeses" % cheese_count 
    print "You have %d boxes of crackers!" % boxes_of_crackers 
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
	

cheese_count = int(raw_input("Please input your cheese count:"))
crackers_count = int (raw_input("Please input your crackers count:"))
print "So, you have %s cheese  and %s crackers:" %(cheese_count, crackers_count)

print "We can even do math inside too:"
cheese_and_crackers(cheese_count+20, crackers_count+19) #TypeError: cannot concatenate 'str' and 'int' objects
#处理方法，1.把变量cheese_count & crackers 定义成int类型； 2. 使用下面的写法
#cheese_and_crackers(cheese_count, crackers_count)

#invalid literal : 无效的文字
'''
ERROR
PS G:\Python_ex> python .\ex19_1.py
Please input your cheese count:jj
Traceback (most recent call last):
  File ".\ex19_1.py", line 10, in <module>
    cheese_count = int(raw_input("Please input your cheese count:"))
ValueError: invalid literal for int() with base 10: 'jj'
PS G:\Python_ex> python .\ex19_1.py
Please input your cheese count:0.9
Traceback (most recent call last):
  File ".\ex19_1.py", line 10, in <module>
    cheese_count = int(raw_input("Please input your cheese count:"))
ValueError: invalid literal for int() with base 10: '0.9'
'''