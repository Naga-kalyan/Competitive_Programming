import pandas as pd
a=input()
b=input()
a=a.split()
b=b.split()
c=[*range(len(a))]
d=[]
for i in range(len(a)):
    if(a[i] not in b):
        d.append(a[i])
    else:
        c.remove(i)
e=pd.Series(d,index=c)
print(e)
