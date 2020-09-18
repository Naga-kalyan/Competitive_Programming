import pandas as pd
a=int(input())
column_names = ["Name", "Age", "Marks","Country"]
result = pd.DataFrame(columns = column_names)
for i in range(0,a):
    b=input()
    result=result.append(pd.Series(b.split(), index=result.columns), ignore_index=True)
result['Marks']=pd.to_numeric(result['Marks'])
for i in range(len(result)):
    if(result['Marks'][i]>result['Marks'].mean()):
        print("0.0")
    else:
        print("1.0")
