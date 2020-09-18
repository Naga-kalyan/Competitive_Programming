a=int(input())
for i in range(0,a):
    b=input()
    b=b.split()
    for j in range(0,2):
        b[j]=int(b[j])
    if((b[0]<0)or(b[1]>100)):
        print("Out of Range")
    elif((b[1]-b[0])!=9):
        print("Difference Not in Range")
    else:
        print([*range(b[0],b[1]+1)])
