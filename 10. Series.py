# 10.1 From ndarray
import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
s = pd.Series(np.random.randn(5), index = ['a','b','c','d','e']) # np.random.randn(5) This creates 5 random numbers.
print(s)
p = s.index # Following function will print the index and its datatype
print(p)

a = pd.Series(np.random.randn(5))
print(a)