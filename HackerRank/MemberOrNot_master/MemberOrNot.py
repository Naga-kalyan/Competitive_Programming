a=input()
b=int(input())
c=[]
e=1
for i in range(0,b):
    d=input()
    c.append(d)
for i in range(0,b):
    if a==c[i]:
        print("True")
        e=2
        break
if(e==1):
    print("False")
