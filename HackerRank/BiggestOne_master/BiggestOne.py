a=int(input())
l=[]
for i in range(0,a):
    l.append(int(input()))
l.sort(reverse = True)
print(l[0])
