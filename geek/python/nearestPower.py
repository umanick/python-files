#
from math import log
def nearestPower(a,b):
	r = log(b, a)
	
	ai = int(r)
	print(ai)
	rem = r - ai
	print(rem)
	if(rem<0.5):
		return b**ai
	else:
		return b**(ai+1)



if __name__ ==  "__main__":
	base = int(input("Enter the base : "))
	power = int(input("Enter the number to verify : "))
	print("Nearest Power of {} to {} is : {}".format(base, power, nearestPower(base,power)))