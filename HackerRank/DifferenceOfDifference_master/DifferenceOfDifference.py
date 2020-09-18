import numpy as np
a=input()
a=a.split()
for i in range(0,len(a)):
    a[i]=float(a[i])
b = [np.nan]+[a[i + 1] - a[i] for i in range(len(a)-1)]
print(b)
c = [np.nan,np.nan]+[b[i + 1] - b[i] for i in range(1,len(b)-1)]
print(c)
