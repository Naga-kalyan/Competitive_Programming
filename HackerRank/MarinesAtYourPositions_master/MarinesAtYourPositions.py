import pandas as pd
a=input()
b=input()
a=a.split()
b=b.split()
c=[]
for i in range(0,len(b)):
    b[i]=int(b[i])
    c.append(a[b[i]])
c=pd.Series(c,index=b)
print(c)
