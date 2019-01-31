for _ in range(int(input())):
    n, r = map(int, input().split())
    c = n-r
    fact = 1
    while(r>0):
        fact = fact*r
        r =r-1

    f=1
    while(n>c):
        f=f*n
        n=n-1
    p=f//fact
    print(p)
    print(p%(10e9+7))