import pandas as pd
import numpy as np

myarray = np.array([[6,9,8,5,4,2],[0,2,5,6,3,9],
                    [8,5,4,1,2,3],[6,9,8,5,4,2],
                    [0,5,3,6,9,8],[8,7,4,5,2,3]])

rownames = ['a', 'b','c','d','e','f']
colnames = ['one', 'two', 'three','four','five','six']

df = pd.DataFrame(myarray, index=rownames, columns=colnames)

print(df)
