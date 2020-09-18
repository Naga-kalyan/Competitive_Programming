import pandas as pd
a=input()
b=input()
a=a.split()
b=b.split()
c=list(set(a+b))
c=sorted(c)
d=[]
e=[]
for i in range(0,len(c)):
    if c[i] not in a or c[i] not in b:
        d.append(c[i])
        e.append(i)
c=pd.Series(d,index=e)
print(c)
