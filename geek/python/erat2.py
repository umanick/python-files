#code
#erat.py


t = 0

def prime(n):
    primes = list(range(2, n))
    for i in range(2, n):
        if(i*i>=n):
            break
        if i in primes:
            for j in (i*2, n, i):
                if j in primes:
                    primes.remove(j)
    print(primes)
                
            
	    

def main():
	t = int(input())
	for i in range(t):
		n = int(input())
		prime(n)


if __name__ == '__main__':
	main()

