import pandas as pd

# # data = pd.Series([0.25, 0.5, 0.75, 1.0])
# # print(data)
# data = pd.Series((3,6,9,8,5,4,2,6,3,5,8))
# # print(data)
# # print(round(data.describe(),2))
# # print(round(data.agg(['max','min','sum','mean','std']),2))
# print(data[1])
# print(data[1:3])

# 
data1 = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])

data2 = pd.Series({'a':1,'b':2,'c':3,'d':4})

print(data1)
print(data2)




