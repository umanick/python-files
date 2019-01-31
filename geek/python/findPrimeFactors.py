#skeleton.py
from math import ceil, sqrt
t = 0

def maxPrimeFactor(n):
	factors = []
	while n % 2 == 0: 
		factors.append(2)
		n = n//2
	top = int(sqrt(n))+1
	for i in range(3, top):
		while n%i==0:
			n = n//i
			factors.append(i)
	if(n>2):
		factors.append(n)
	#print(factors)
	return sorted(factors, reverse=True)[0]

def isPrime(n):
	top = int(sqrt(n))+1
	for i in range(2, top):
		if n%i==0:
			return False
	return True

def findMaxPrimeFactor(n):
	top = int(sqrt(n))+1
	#print('top = {}'.format(top))
	for i in range(top, 1, -1):
		#print('i = {}'.format(i))
		if not isPrime(i):
			continue
		if n%i==0:
			return i
	return n

def main():
	t = int(input())
	outputs = []
	while t>0:
		n = int(input())
		#primeFactors(n)
		outputs.append(findMaxPrimeFactor(n))
		t-=1
	for x in outputs:
		print(x)
main()