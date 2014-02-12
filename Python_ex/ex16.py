# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename #如果文件不存在，将新建一个文件
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate() #清空目标文件
"""
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."


'''
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''
#把多个target.write整合成一个（一下两种方法都可行）
#target.write(line1+"\n"+line2+"\n"+line3+"\n")
#target.write("%r\n%r\n%r\n" %(line1,line2,line3))
target.write("%s + \n + %s + \n +  %s + \n" % (line1, line2, line3))

print "And finally, we close it."
"""
target.close()
