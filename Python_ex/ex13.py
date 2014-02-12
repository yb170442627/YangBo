# -*- coding: utf-8 -*-

from sys import argv
#argv和raw_input()的区别： argv的参数是在执行程序的时候一并带上，raw_input()是获取用户输入的信息作为参数。
script, first, second, third = argv

script = raw_input("Your script is:")

print "So, you script is %s:" %script

print "The script is called:", script # print 后面跟的字符串中若不包含格式符号(%d,%s, %r等)，则需要字符串和变量之间需要用逗号来分隔
#若有格式符号，则直接用"%" 连接
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#在执行该脚本的时候，需要传递“三个”参数(这三个参数可以任意)， 分别对 first , second , third 赋值。
#如果参数不够，报错：ValueError: need more than 2 values to unpack
#如果参数过多，报错：ValueError: too many values to unpack
#为什么不是四个参数？ script 获取的是改程序的名称： ex13.py
#为什么输出结果中script的值是22？ 那是因为加入了raw_input()函数，并且对script重新赋值，它获得是用户输入
#的信息，即：22

'''
The output is as follows:
PS F:\Python_ex> python .\ex13.py 1 2 3
Your script is:22
So, you script is 22:
The script is called: 22
Your first variable is: 1
Your second variable is: 2
Your third variable is: 3
'''