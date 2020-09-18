a=int(input())
c=[]
for i in range(0,a):
    b=input()
    c.append(len(b))
c.sort(reverse=True)
print(c[0])
