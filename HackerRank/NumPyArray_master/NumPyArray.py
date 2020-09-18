import numpy as np
a=int(input())
b=int(input())
c=int(input())
d=[*range(a,b+1,c)]
if(c<b and a<b):
    for i in d:
        print(i)
else:
    print("Constraints are failing!") 
