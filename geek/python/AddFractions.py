#AddFractions.py

def gcd(a,b):
	times2 = 0

	if (a == 0): return b
	if (b == 0): return a

	while  ((a | b) & 1) == 0:
		a >>= 1
		b >>= 1
		times2+=1

	while ((a & 1) == 0):
		a >>= 1;

	while b!=0:
		while ((b & 1) == 0) :
		   b >>= 1;

		if (a > b) :
			t = b
			b = a
			a = t

		b = b - a; 
	

	return a << times2

def lcm(a, b):
	return (a*b)//gcd(a, b)

#Your task is to complete this function
#Your shouldn't return any thing it should print the required output
def addFraction(num1, den1, num2, den2):
	num3 = 0
	if(den1==den2):
		num3 = num1+num2
		den3 = den1
	else:
		den3 = lcm(den1, den2)
		num3 = num1*(den3//den1) + num2*(den3//den2)

	#Find GCD
	g = gcd(num3, den3)
	if g > 1:
		num3 = num3//g
		den3 = den3//g
	print(num3, end= '/')
	print(den3)

	

def main():
	t = int(input())
	for i in range(t):
		nums = input().split()
		addFraction(int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3]))


if __name__ == '__main__':
	main()