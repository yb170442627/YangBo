# -*- coding: utf-8 -*-

cities = {'SH': 'ShangHai', 'BJ': 'BeiJing','GZ': 'GanZhou'}

cities['GD'] = 'GuangDong'
cities['SD'] = 'ShanDong'

def find_city(themap, state):
    if state in themap:
	    return themap[state]
    else:
	    return "Not Found."
		
cities['_find'] = find_city


while True:
    print "State?(ENTER to quit)",
    state = raw_input("> ")
    if not state: break
	
    city_found = cities['_find'](cities,state)
    print city_found