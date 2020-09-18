a=int(input())
for i in range(0,a):
    b=int(input())
    if((b%2!=0)and(b%3==0)):
        print("Matrix")
    elif((b%2!=0)):
        print("Glitch")
    elif((b%2==0)and(b%3==0)):
        print("Zion")
    else:
        print("Reality")
