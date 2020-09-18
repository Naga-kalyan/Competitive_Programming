a=int(input())
for i in range(0,a):
    b=0
    c=int(input())
    for j in range(0,c):
        k=c-j-1
        for i in range(0,k):
            print(" ",end='')
        b=b+(10**j)
        print(b**2)
    print()
