def nCr(n, r, c, m): 
    fr = fact(r)
    f=1
    while(n>c):
        f=f*n
        n=n-1
    return (f // fr)%m
  
# Returns factorial of n 
def fact(n): 
  
    res = 1
      
    for i in range(2, n+1): 
        res = res * i 
          
    return res 


def main():
    t = int(input())
    outputs = []
    for i in range(t):
        ncr = input().split()
        n = int(ncr[0])
        r = int(ncr[1])
        c = n-r
        if(n>r):
            outputs.append(nCr(n, r, c, 1000000007))
        else:
            outputs.append(0)
    for x in outputs:
        print(x)

if __name__ == '__main__':
    main()

