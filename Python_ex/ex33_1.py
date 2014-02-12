# -*- coding: utf-8 -*-

def append_num(num):   # 定义了一个append_num(num）函数
    i = 0              # 声明了一个常量 i
    numbers = []       # 声明了一个空的列表 numbers = []
    while i < num:     # 执行while循环
        print "At the top i is %d" % i
        numbers.append(i) #调用列表的append方法，当i< num成立的时候，把i的值追加到numbers这个空的列表中
        i = i + 1 # i + 1
    return numbers # 返回 numbers 的值。给谁呢？给下面list这个变量。 
	                #为什么？因为list这个变量调用了append_num(num）函数.
					# 它把 6 这个参数传递给了append_num(num）函数，函数最终返回结果给list这个变量
	
	
list = append_num(6)

print list

#Python 词汇return 来将变量设置为“一个函数的值”