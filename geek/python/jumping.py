#code

def isJumping(num):
    pd = num%10
    num //=10
    flag = True
    while num>=10:
        d = num%10
        print(flag, pd, d, num)
        num //=10
        if abs(pd-d)!=1:
            flag = False
            break
        pd = d
    print(flag, pd, num)
    if flag and abs(pd-num)==1:
        return True
    else:
        return False
def isJumping2(num):
    nl = map(str, str(num))
    x = nl[0]
    for i in range(1,len(nl)):
        y = nl[i]
        if abs(int(x)-int(y))!=1:
            return False
        x = y
    return True
def findAllJumping(n):
    list = []
    for i in range(n+1):
        if i<11:
            list.append(i)
        elif isJumping2(i):
            list.append(i)
    return list

def main():
    t = int(input())
    outputs = []
    for i in range(t):
        n = int(input())
        outputs.append(findAllJumping(n))
    for x in outputs:
        print(x)
def main2():
    n = int(input())
    print(findAllJumping(n))
    #print(isJumping2(n))
if __name__ == '__main__':
    main2()
'''
def isJumping(num):
    pd = num%10
    num //=10
    flag = True
    while num>10:
        d = num%10
        num //=10
        if abs(pd-d)>1:
            flag = False
            break
        pd = d
    if flag and abs(pd-num)==1:
        return True
    else:
        return False
    
def findAllJumping(n):
    list = []
    for i in range(n+1):
        if i<11:
            list.append(i)
        elif isJumping(i):
            list.append(i)
    return list

def main():
    t = int(input())
    inputs = []
    outputs = {}
    for i in range(t):
        n = int(input())
        inputs.append(n)
    maxn = max(inputs)
    jumpMax = findAllJumping(maxn)
    outputs[maxn] = jumpMax
    for n in inputs:
        if n in outputs:
            continue
        list = []
        for x in jumpMax:
            if x <= n:
                list.append(x)
            else:
                break
        outputs[n] = list

    for x in inputs:
        print(' '.join(map(str, outputs[x])))

if __name__ == '__main__':
    main()
'''