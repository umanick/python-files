#25_import_fns.py

def break_em(stuff):
	"""This function will break up words for you."""
	words = stuff.split(' ')
	return words

def sort_em(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off"""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off"""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	""""Takes in a full sentence and returns the sorted words"""
	words = break_em(sentence)
	return sort_em(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_em(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_last_sorted(sentence):
	"""Sorts the words first and then prints the first and last one"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)