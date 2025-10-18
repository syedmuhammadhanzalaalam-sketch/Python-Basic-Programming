import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
d = {
    'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
    'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(d)
print(df)
pd.DataFrame(d, index = ['d', 'b', 'a']) # a data frame will be constructed for given row labels
pd.DataFrame(d, index = ['d', 'b', 'a'], columns= ['two', 'three']) # shows a data frame when we give coloumn labels
df.columns

# 11.2 From dict of ndarrays / lists
d = {
    'one' : [1.,2.,3.,4.],
    'two' : [4.,3.,2.,1.],
}
pd.DataFrame(d)
pd.DataFrame (d, index = ['a', 'b', 'c', 'd'])

# 11.3 From a list of dicts
data2 = [{'a' : 1, 'b': 2}, {'a': 5, 'b' : 10, 'c' : 20}]
pd.DataFrame(data2)
pd.DataFrame(data2, index=['first', 'second'])
pd.DataFrame(data2, columns=['a', 'b'])

# Fixed usage for multi-index DataFrame from dictionary of dictionaries:
multi_index_df = pd.DataFrame({
    ('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
    ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
    ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
    ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
    ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10},
})
print(multi_index_df)

# 11.5 Alternate Constructors
data = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
print(data)

pd.DataFrame.from_records(data, index='C')

pd.DataFrame(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]))

df['one']

df['three'] = df['one'] * df['two'] 

df['flag'] = df['one'] > 2 
print(df)

# Remove the 'two' column from the DataFrame
del df['two']  # delete a column 'two' from data frame

# Pop the 'three' column from the DataFrame and store it in variable 'three'
three = df.pop('three')  # Pop the 'three' column from the DataFrame and store it in variable 'three'

print(df)

df['foo'] = 'bar'  # Add a new column 'foo' with all values set to 'bar'
print(df)

# following example will take values from column one up to the given range and will populate the new column
df['one_trunc'] = df['one'].copy()
df.loc[df.index[2]:, 'one_trunc'] = np.nan  # set NaN for rows after the first two

print(df)
print(df)

# The insert() function has three arguments:
# 1. The index at which the new column will be inserted.
# 2. The label or title of the new column.
# 3. The data to populate the new column.
df.insert(1, 'bar2', df['one'])

print(df)

# Access row with label 'b' (if exists in index)
if 'b' in df.index:
    print(df.loc['b'])  # Returns the column labels and values for row label 'b'
else:
    print("Row label 'b' not found in index.")

# Access the third row by integer location
try:
    print(df.iloc[2])  # Returns the values of the third row (index 2)
except IndexError:
    print("Row index 2 is out of range.")

df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])

df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])

# add values of respective column labels
result_add = df + df2

# subtract the first row of df from all rows in df
result_sub = df - df.iloc[0]

print(df * 5 + 2)

print(1 / df)

print(df ** 4)

df1 = pd.DataFrame({'a': [1, 0, 1], 'b': [0, 1, 1]}, dtype=bool)

df2 = pd.DataFrame({'a': [0, 1, 1], 'b': [1, 1, 0]}, dtype=bool)

df3 = pd.DataFrame({'a': [0, 1, 1], 'b': [1, 1, 0]}, dtype=bool)
print(df3)

# Bitwise NOT operator on boolean DataFrame
print(~df1)

# Bitwise OR operator on boolean DataFrames
print(df1 | df2)  # or operator

print(df1 & df2)  # and logical operator

# only show the first 5 rows
# Display the first 5 rows, transposed
print(df.head().T)

# Create a date range and display it
dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

print(df)

df2 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
})

print(df2)

# Having specific dtypes
print(df2.dtypes)

# display first 5 records
print(df.head())

# display last 3 records
print(df.tail(3))

# display indexes
print(df.index)

# display columns
print(df.columns)

# print values
print(df.values)
# Transposing your data
print(df.T)
# Sorting by an axis
# Sorting by column labels in descending order
print(df.sort_index(axis=1, ascending=False))

# Sorting by values in column 'B'
print(df.sort_values(by='B'))
# Describe shows a quick statistic summary of your data
print(df.describe())
# Selecting a single column, which yields a Series, equivalent to df.A
# Selecting a single column, which yields a Series, equivalent to df.A
print(df['A'])

# Selecting via [], which slices the rows.
print(df[0:3])
# Selecting via label slicing for rows between '20130102' and '20130104'
print(df.loc['20130102':'20130104'])

# Selecting on a multi-axis by label
print(df.loc[:, ['A', 'B']])
# Showing label slicing, both endpoints are included
print(df.loc['20130102':'20130104', ['A', 'B']])
# Reduction in the dimensions of the returned object
print(df.loc['20130102', ['A', 'B']])

# For getting a scalar value
print(df.loc[dates[0], 'A'])
# For getting fast access to a scalar
# For getting fast access to a scalar
print(df.at[dates[0], 'A'])

# Select via the position of the passed integers
print(df.iloc[3])
# By integer slices, acting similar to numpy/python
print(df.iloc[3:5, 0:2])
# By lists of integer position locations, similar to the numpy/python style
print(df.iloc[[1, 2, 4], [0, 2]])

# For slicing rows explicitly
print(df.iloc[:, 1:3])

# For getting a value explicitly
# For getting a value explicitly
print(df.iloc[1, 1])

# Using a single column’s values to select data.
print(df[df['A'] > 0])
# Using the isin() method for filtering:
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)

# Selecting values from a DataFrame where a boolean condition is met.
print(df[df > 0])
df2[df2['E'].isin(['two', 'four'])]
