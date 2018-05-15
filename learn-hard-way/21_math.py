def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

def mod(a, b):
	print "MODING %d %% %d" % (a, b)
	return a % b

print "Let's do some math with just functions!"

age = add(30, 7)
height = subtract(72, 4)
weight = multiply(75, 2)
iq = divide(320, 2)
ageagain = mod(77, 40)

print "Age: %d, Height: %d, Weight: %d, IQ: %d, Age : %d" % (age, height, weight, iq, ageagain)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, mod(8, 3)))))

print "That becomes: ", what, "Can you do it by hand?"