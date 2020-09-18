a=int(input())
for i in range(0,a):
    b=input()
    b=b.split()
    b[0]=int(b[0])
    b[1]=int(b[1])
    if((b[0]<1)or(b[1]<1)or(b[0]>1000)or(b[1]>1000)):
        print("Out of Range!")
    else:
        g=b[1]
        while(1):
            if((g%b[0]==0)and(g%b[1]==0)):
                print(g)
                break
            else:
                g=g+1
