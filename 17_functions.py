def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "no input"

print_two("Hey", "Upie")
print_two_again("Ca", "Va")
print_one('Bonjour')
print_none()

def cheese_and_crackers(cc, crc):
	print "We have %d cheeses" % cc
	print "We have %d boxes of crackers" % crc

cheese_and_crackers(10, 20)


cheese_and_crackers(10+10, 20+20)

a = 10
b = 12
cheese_and_crackers(a, b)

cheese_and_crackers(a+2, b+3)

print "." * 40
