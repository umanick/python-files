#nearestPower2.py
def nearestPower2(b, n):
	i = 0
	an = n
	if b<2:
		return 1
	while n>0:
		n = n//b
		i+=1
	minpower = b**(i-1)
	maxpower = b**i
	med = (minpower+maxpower)/2
	if(med>an):
		return minpower
	else:
		return maxpower

def nearestPower3(a, b):
	i = 0
	an = b
	if a<2:
		return 1
	while b>0:
		b = b//a
		i+=1
	minpower = a**(i-1)
	maxpower = a**i
	med = (minpower+maxpower)/2
	if(med>an):
		return minpower
	else:
		return maxpower

def main():
	b = int(input('Base? : '))
	n = int(input('Number? : '))
	print("Nearest Power of {} to {} is {}".format(b, n, nearestPower3(b,n)))

if __name__ == "__main__":
	main()

