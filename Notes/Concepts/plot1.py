import matplotlib.pyplot as plt
import numpy as np

def f1(x):  return x**4 - 4*x**2 + 3*x
def f2(x):  return np.sin(10*x)*10
x = np.linspace(-3,3,1000)
plt.plot(x,f1(x),x,f2(x))
