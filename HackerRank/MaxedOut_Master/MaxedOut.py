a=[1, 7, 90, 33, 67, 56, 20, 39, 10, 30]
b=int(input())
for i in range(0,b):
    d=input()
    d=d.split()
    for j in range(0,3):
        d[j]=int(d[j])
    if((a[d[0]]>a[d[1]])and(a[d[0]]>a[d[2]])):
        print(a[d[0]])
    elif((a[d[1]]>a[d[0]])and(a[d[1]]>a[d[2]])):
        print(a[d[1]])
    else:
        print(a[d[2]])
