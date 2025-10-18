# Lists
list1 = ['Hanzala','2005']
print(list1)

# Accessing values in Lists
list1 = ['math','urdu','english','science']
list2 = [1,2,3,4,5]
print("list1[1]:",list1[0])
print("list2[1:5]:",list2[1:5])

# Updating Lists
list1 = ['math','urdu','2006','2006']
list1[1] = 'english'
print(list1)
list1.append('Hanzala') #.append() is a function used to add something to the end of the list.
print(list1)

# Delete List element 
list1 = ['math','urdu','english','science']
print(list1)
del list1[0]
print(list1)

# 2nd way to delete List element
list1 = ['math','urdu','english','science']
print(list1)
list1.remove('science')
print(list1)    