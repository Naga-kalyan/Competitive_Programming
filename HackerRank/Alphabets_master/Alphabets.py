import pandas as pd
b=input()
inp = 'abcedfghijklmnopqrstuvwxyz'
a=[]
for i in range(0,len(inp)):
    a.append(inp[i])
c=pd.Series(a,name=b)
print(c)
