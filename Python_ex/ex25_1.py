# -*- coding: utf-8 -*-

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

	
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
	
	
words = "where are you come from?"
word = break_words(words)
print word

word1 = sort_words(word)
print word1
