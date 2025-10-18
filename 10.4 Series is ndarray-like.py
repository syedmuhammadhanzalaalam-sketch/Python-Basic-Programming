import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
s[0] #access single value
s[:5]  #access range of values
s[s > s.median()] # return a range of values in series whose value is greater than the median
s[[4,3,1]] # return the values in series with indexes. 4,3,1 are the positions of the indexs For example: the index at 4,3,1 are e,d,b respectively
np.exp(s) # returns the exponent values. just like e^a (here a is index and its respective data is placed here
s['a'] # Following example will get the data of given index
s['e'] = 12 # update the data of the given index
s
'e' in s # return true if 'e' is in the values of index otherwise false
s['f']
s.get('f') # it will return none
s.get('f', np.nan) # it will return default value