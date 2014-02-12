# -*- coding: utf-8 -*-

from sys import argv

script , filename = argv
#open这个函数会接受一个参数（程序执行时输入的文件名），并且返回一个值（文件句柄）；
#我们将这个值赋予txt这个变量
txt = open (filename)

print "Opening your file: %r" % filename
#直接调用read()方法，读取文件内容，并打印出来
print txt.read()
#文件打开后，记得关闭
txt.close()

print "Opening your file again."
#使用raw_input请用户用人机交互的方式输入文件名，注意raw_input方法的输入参数”>”，
#是一种用户提示，提示用户在提示符”>”后输入要求的内容
file_again = raw_input("> ")
#定义一个txt_again变量来获得文件句柄
txt_again = open(file_again)
#读取文件内容并打印在屏幕上
print txt_again.read()
#关闭文件
txt_again.close()