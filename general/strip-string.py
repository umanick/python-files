import sys

string = 'Alice"s; -'
front = False
left = right = mid = 0
for c in string:
    print c, right, mid
    if not front and c.isalnum():
        front = True
        left += 1
    if not c.isalnum():
        mid = right - 1
    else:
        mid = right + 1
    right += 1    

print left
print right
print mid
print string[left-1:mid+1]