import pandas as pd
import numpy as np

n = input().split()
ser = pd.Series(n)
print(ser.value_counts().sort_index())
