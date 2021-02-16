import pandas as pd

# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print(data)
data = pd.Series((0.25, 0.5, 0.75, 1.0))
print(data,type(data))
print(data.values)
print(data.index)
print(data.keys)

