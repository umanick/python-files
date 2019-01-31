import sys

string = '---?'
front = False
index = 0
right = left = 0
for c in string:
    if c.isalnum():
        right = index
        if not front:
            left = index
            front = True
    index += 1
if front:
    print string[left:right+1]
else:
    print string