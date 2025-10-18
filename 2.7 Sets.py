# Sets
list1 = [1, 2, 3, 4, 5]
print ((type) list1)
myset = set(list1)
print(myset)
print ((type) myset)

# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed data types 
my_set = {1, 'hello', 1.2, 'c'}

# adding a single value
my_set.add('hanzala')
print(my_set)

# adding multiple values
my_set.update(list1)
print(my_set)

# Raisa Value
my_set.discard ('1.2') # it will not raise an error
my_set.remove ('1.2') # it will raise an error 