def scan(sentence):
	direction = 'direction'
	verb = 'verb'
	stop = 'stop'
	noun = 'noun'
	number = 'number'
	words = sentence.split()
	result = []
	directions = ['north', 'west', 'south', 'east']
	verbs = ['go', 'stop', 'kill', 'eat']
	stops = ['the', 'in', 'of', 'from', 'at', 'it']
	nouns = ['door', 'bear', 'princess', 'cabinet']
	for word in words: 
		temp = ()
		if word.lower() in directions:
			temp = (direction, word)
		elif word.lower() in verbs:
			temp = (verb, word)
		elif word.lower() in stops:
			temp = (stop, word)
		elif word.lower() in nouns:
			temp = (noun, word)
		else:
			try:
				num = int(word)
				temp = (number, num)
			except ValueError:
				temp = ('error', word)

		result.append(temp)
	return result