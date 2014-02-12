# -*- coding: utf-8 -*-

from sys import argv

script, input_file = argv

#定义一个print_all的方法，f为参数（执行程序时输入的文件名），打印文件的所有内容
def print_all(f):
    print f.read()
	
'''	
定义一个rewind方法，调用python里file自带的seek方法，并把参数设置成"0". 
作用是：seek() 函数的处理对象是 字节 而非行，所以 seek(0) 只是转到文件的 0 byte，也就
是第一个 byte 的位置.
'''	

def rewind(f):
    f.seek(0)
	
#定义了一个print_a_line方法，里面有两个参数， （行号，文件名）
def print_a_line(line_count, f):
    print line_count, f.readline() # reandline()打印一行内容
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

#声明一个current_line的变量，并赋值为“1”。 表示文件从第一行开始
current_line = 1
print_a_line(current_line, current_file),

current_line = current_line + 1
print_a_line(current_line, current_file),

current_line += current_line # current_line = current_line + current_line (经过上面两次的叠加 ，current_line的值变成了2，所以此时的值为“4”)
print_a_line(current_line, current_file),

'''The output is as follows:

PS G:\Python_ex> python .\ex20.py test.txt
First let's print the whole file:

cat  /proc/cpuinfo
Cat /proc/meminfo
Fdisk –l
AAAAAAAAAAAAAAAAAAAAAAAA
BBBBBBBBBBBBBBBBBBBBBBB
CCCCCCCCCCCCCCCCCCCCCCCCCC
DDDDDDDDDDDDDDD
FFFFFFFFFFFFFFF
EEEEEEEEEEEE
Now let's rewind, kind of like a tape.
Let's print three lines:
1 cat  /proc/cpuinfo

2 Cat /proc/meminfo

4 Fdisk –l '''

