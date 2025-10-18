import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
s+s
s * 2
s = pd.Series(np.random.randn(5), name = 'somethig')
s
s.name
s2 = s.rename('Different')
s2.name