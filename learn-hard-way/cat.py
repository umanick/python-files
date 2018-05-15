tabby_cat="\tI'm tabbed in."
persian_cat="I'm split\non a line."
backslash_cat="I'm \\ a \\ cat."

fat_cat="""
I'll do a list: \v
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

yn = raw_input('Wanna play?')
#while True:
if yn == 'y':
	while True:
		for j in [1,2,3,4,5,6,7,8,9,10]:
			for i in ["/","- ","|","\\","|"]:
				print "%s\r" % i,