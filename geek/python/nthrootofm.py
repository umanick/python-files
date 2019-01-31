

t = 0

def nthroot(n,m):
    o = m**(1/n)
    oround = abs(round(o) - o)
    if oround>0.001:
        return -1
    else:
        return round(o)

def main():
    t = int(input())
    outputs = []
    for i in range(t):
        nm = input()
        nml = nm.split()
        n = int(nml[0])
        m = int(nml[1])
        outputs.append(nthroot(n,m))
    for x in outputs:
        print(x)
if __name__ == '__main__':
	main()

