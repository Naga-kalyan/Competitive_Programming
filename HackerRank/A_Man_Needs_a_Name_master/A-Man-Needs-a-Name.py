import pandas as pd
a=input()
b=input()
c=input()
c=c.split()
c[0]=int(c[0])
c[1]=int(c[1])
d=pd.Series(a.split(),name=b)
if(c[1]==1):
    print(d[:c[0]])
else:
    print(d[len(d)-c[0]:])
