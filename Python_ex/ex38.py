# -*- coding: utf-8 -*-

ten_things = "Apples|Oranges|Crows|Telephone|Light|Sugar"

print "Wait there's not 10 things in that list , let's fix that."

stuff = ten_things.split('|') #按空格来分隔

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
  next_one = more_stuff.pop()
  print "Adding: ", next_one
  stuff.append(next_one)
  print "There's %d itmes now." %len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop() # 弹出列表里面的最后一个元素
print ' '.join(stuff)
print '#'.join(stuff[3:4])
