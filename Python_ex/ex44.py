# -*- coding: utf-8 -*-

class other(object):

  def override(self):
    print "OTHER override()"
	
  def implicit(self):
    print "OTHER implicit()"
	
  def altered(self):
    print "OTHER altered()"
	
class Child(object):

  def __init__(self):
    self.other = other()
	
  def implicit(self):
    self.other.implicit()
	
  def override(self):
    print "CHILD override()"
	
  def altered(self):
    print "CHILD, BEFORE OTHER altered()"
    self.other.altered()
    print "CHILD, AFTER OTHER altered()"
	
son = Child()

son.implicit()
son.override()
son.altered()


'''
The output is as follows:

PS F:\Python_ex> python .\ex44.py
OTHER implicit()
CHILD override()
CHILD, BEFORE OTHER altered()
OTHER altered()
CHILD, AFTER OTHER altered()

'''
