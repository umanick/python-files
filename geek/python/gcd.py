def gcd(a,b):
	times2 = 0

	if (a == 0): return b
	if (b == 0): return a

	while  ((a | b) & 1) == 0:
		a >>= 1
		b >>= 1
		times2+=1

	while ((a & 1) == 0):
		a >>= 1;

	while b!=0:
		while ((b & 1) == 0) :
		   b >>= 1;

		if (a > b) :
			t = b
			b = a
			a = t

		b = b - a; 
	

	return a << times2

if __name__ == '__main__':
	a = int(input('First Number: '))
	b = int(input('2nd Number: '))
	print('GCD of {} & {} is {}'.format(a, b, gcd(a, b)))