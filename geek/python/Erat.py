#Erat.py

def erat(n):
	primes2 = list(range(2,n))  
	p = 2
	while p*p < n:
		if p in primes2:
			for i in range(p*p, n+1, p):
				if i in primes2:
					primes2.remove(i)
		p+=1
	print(primes2)
	

def main():
	t = int(input())
	for i in range(t):
		n = int(input())
		erat(n)


if __name__ == '__main__':
	main()