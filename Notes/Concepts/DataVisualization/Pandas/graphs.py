import pandas as pd
data = pd.Series((3,6,9,8,5,4,2,6,3,5,8))

# data.plot()
# data.plot(kind='line')  
# data.plot(kind='pie')  
# data.plot(kind='barh')  
# data.plot(kind='hist')
# data.plot(kind='box')
data.plot(kind='kde')
