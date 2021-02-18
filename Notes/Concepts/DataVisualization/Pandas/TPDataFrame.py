import pandas as pd
import numpy as np

# w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
# x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
# y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
# z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})


# grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})

# print(grades)
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})


grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})

print(grades)
print(grades.T)
print(grades['Chemistry'])
print("keys : ",grades.keys())
print("values : ", grades.values)
print(grades.stack())


