a=int(input())
for i in range(0,a):
    b=int(input())
    if(b<2 or b>1000):
        print("Out of Range")
    else:
        z=0
        for j in range(2,b):
            if(b%j==0):
                z=1
                break
        if(z==0):
            print("PRIME")
        else:
            print("COMPOSITE")
