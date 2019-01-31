from math import ceil, log
t = 0
                
def ncubeandb(n):
	crn = 1
	if(n>2):
		crn = ceil((n**(1/3)))#ceil(log(n,3))
	aandb = []
	for a in range(1,crn+1):
		for b in range(0, crn+1):
 			if(a**3 + b**3) == n:
 				aandb.append((a,b))
	print(len(aandb))

def main():
	t = int(input())
	for i in range(t):
		n = int(input())
		ncubeandb(n)

if __name__ == '__main__':
	main()