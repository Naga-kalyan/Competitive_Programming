import re
a=int(input())
for _ in range(a):
    b=input()
    z=re.match(r'\w+\s<[a-z](\w|-|\.|_)+@[a-z]+\.[a-z]{1,3}>',b)
    if(z):
        print(b)
