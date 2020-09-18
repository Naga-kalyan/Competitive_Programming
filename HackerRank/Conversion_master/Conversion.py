import numpy as np
import pandas as pd
a=input()
a=a.split()
input_list=input()
input_list=input_list.split()
m = int(a[0])
n = int(a[1])
if m*n == len(input_list):
    c=np.array(input_list)
    d=c.reshape(m,n)
    e=pd.DataFrame(d)
    print(e)
else:
    print("Weird Order!")
