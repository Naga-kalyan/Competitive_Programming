import re
a=int(input())
for i in range(a):
    b=input()
    z=re.match('[7-9]\d{9}',b)
    if (z) and (len(b)==10):
        print('YES')
    else:
        print('NO')
