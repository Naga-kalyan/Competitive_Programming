T = int(input())
a=list(map(int,input().split()))
for i in range(0,T):
    b = input()
    if(b == '+'):
        print(a[0]+a[1])
    elif(b == '-'):
        print(a[0]-a[1]) 
    elif(b == '*'):
        print(a[0]*a[1])
    elif(b == '/'):
        print(a[0]//a[1]) 
    elif(b == '%'):
        print(a[0]%a[1])
