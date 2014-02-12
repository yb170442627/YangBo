# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line too, how?
in_file = open(from_file)
#print in_file.read()

indata = in_file.read()

print "The input file is %d bytes long" % len(indata) # "len(str)" 得到字符串的长度

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("? ")


#out_file = open(to_file,'w') # IOError: File not open for reading
out_file = open(to_file,'w+') # 使用"w+"可以让写入的文件可读。
out_file.write(indata)
#print out_file.read()


print "Alright, all done."

out_file.close()
in_file.close()


