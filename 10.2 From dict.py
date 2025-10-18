import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
d = {'a' : 0., 'b' : 1., 'c' : 2.} 
pd.Series(d)

a = pd.Series(d, index = ['b', 'c', 'd', 'a'])
print(a)