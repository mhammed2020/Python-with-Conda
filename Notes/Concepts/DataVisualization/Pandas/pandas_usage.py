import pandas as pd

# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print(data)
data = pd.Series((3,6,9,8,5,4,2,6,3,5,8))
# print(data)
# print(round(data.describe(),2))
print(round(data.agg(['max','min','sum','mean','std']),2))

