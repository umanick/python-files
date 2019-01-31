#skeleton.py

from math import ceil
t = 0

def perfect(n):
    sum = 1
    for i in range(2,n):
        if(n % i == 0):
            sum = sum + i
            print(i, end = ',')
    print()
    print("sum = {}".format(sum))
    if (sum == n):
        print(1)
    else:
        print(0)


def perfect2(n):
    sum = 1
    for i in range(2, n):
        if i*i>=n:
            break
        if(n % i == 0):
            sum = sum + i + n/i
    if (sum == n):
        print(1)
    else:
        print(0)

def main():
    t = int(input())
    inputs = []
    for i in range(t):
        inputs.append(int(input()))
    for x in inputs:
        perfect(x)
        perfect2(x)


if __name__ == '__main__':
    main()

