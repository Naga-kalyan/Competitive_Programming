import pandas as pd
import numpy as np

# Write the logic to take inputs from STDIN
a=input()
a=a.split()
b=input()
c=input()
d=input()
d=d.split()
# The following parameters wiill be required. You can take additional parameters as per your requirement
stp =int(a[0])
enp =int(a[1])
step =int(a[2])
list2 =c.split()
n =int(d[0]) 
pos =int(d[1])

# Write the logic to perform operations
list1 = np.arange(stp,enp,step) # Write the paramters for the arange function
df = pd.DataFrame({list2[0]:pd.Series(list1),list2[1]:pd.Series(b.split())})
if(pos==1):
    print(df.head(n))
else:
    print(df.tail(n))
