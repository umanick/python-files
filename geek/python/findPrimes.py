def findPrimes(givenNumber):
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

    return genPrime

def main():
    t = int(input())
    primes = []
    lt = 0
    dic = {}
    inputs = []
    for i in range(t):
        inputs.append(int(input()))
    sinputs = sorted(inputs, reverse=True)
    n = sinputs[0]
    primes = findPrimes(n)
    primes.sort(reverse=True)
    dic[n] = sum(primes)
    for i in range(1, len(sinputs)):
        n = sinputs[i]
        if n in dic:
            continue
        newprimes = list(primes)
        for x in primes:
            if x > n:
                newprimes.remove(x)
            else:
                break
        dic[n] = sum(newprimes)
    for n in inputs:
        print(dic[n])

        

if __name__ == '__main__':
    main()