from collections import deque
t = int(input())

# Store the original input sequence
originalInput = []
for i in range(t):
    originalInput.append(int(input()))

# Create a queue with sorted elements from input
inputQueue = deque(sorted(originalInput, reverse=True))

# Find the set of non-Prime numbers up to the largest input with SoE
n = inputQueue[0]
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
genPrime = filter(lambda x: x not in notPrime, range(1, n+1))

# Sum up primes in a loop and record answers along the way
sumPrimes = 0
answers = {}
for p in genPrime:
    while p > inputQueue[-1]:
        answers[inputQueue.pop()] = sumPrimes
    sumPrimes += p
while inputQueue:
    answers[inputQueue.pop()] = sumPrimes

# Map answers back to original input order
for a in map(lambda i: answers[i], originalInput):
    print(a)