import timeit
t = 0
                
def erat(n):
    primes2 = list(range(2,n+1))
    p = 2
    while p*p < n:
        if p in primes2:
            for i in range(p*p, n+1, p):
                if i in primes2:
                    primes2.remove(i)
        p+=1
    return sum(primes2)

def primeSum1(givenNumber):  
    
    # Initialize a list
    #primes = []
    sum = 0
    for possiblePrime in range(2, givenNumber + 1):
        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            #primes.append(possiblePrime)
            sum += possiblePrime
    
    return(sum)

def primeSum2(givenNumber):
    n = givenNumber
    notPrime = set([1])
    cur = 2
    while cur <= n:
        i = 2
        while i*cur <= n:
            notPrime.add(cur*i)
            i += 1
        cur += 1
        while cur in notPrime:
            cur += 1

    # Generate prime numbers from non-prime
    genPrime = list(filter(lambda x: x not in notPrime, range(1, n+1)))

    return sum(genPrime)

def main():
    t = int(input())
    print(timeit.timeit('erat({})'.format(t), globals=globals(), number=10000))
    print(timeit.timeit('primeSum1({})'.format(t), globals=globals(), number=10000))
    print(timeit.timeit('primeSum2({})'.format(t), globals=globals(), number=10000))

if __name__ == '__main__':
    main()