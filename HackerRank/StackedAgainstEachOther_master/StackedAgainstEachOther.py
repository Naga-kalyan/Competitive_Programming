import pandas as pd
import numpy as np
a=input()
b=input()
a=a.split()
b=b.split()
d={0:pd.Series(a),1:pd.Series(b)}
c=pd.DataFrame(d)
print(c)
