import matplotlib.pyplot as plt 
import numpy as np

x = np.arange(0,10,0.01)

def f(x):
    return np.sqrt(x * (x-1) * (x-1))

print(x, f(x))
plt.plot(x, f(x), "b")
plt.plot(x, -f(x), "b")
plt.show()