a=input()
a=a.split(",")
for i in range(0,len(a)):
    a[i]=int(a[i])
a=sorted(a)
print(a[len(a)-2])
