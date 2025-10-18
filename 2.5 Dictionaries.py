# Accessing value in Dictionary
dict = {'Name' : "Syed Hanzala Alam", 'Depart' : "Embedded", 'Section' : "A"}
print(dict['Section'])

# Updating Dictionary
dict = {'Name' : "Syed Hanzala Alam", 'Depart' : "Embedded", 'Section' : "A"}
print(dict)
dict['Section'] = "B"
print(dict)
dict['University'] = "University of Lahore"
print(dict)

# Delete Dictionary Element
dict = {'Name' : "Syed Hanzala Alam", 'Depart' : "Embedded", 'Section' : "A"}
print(dict)
del dict ['Section']
print(dict)

# Clear Dictionary Element
dict = {'Name' : "Syed Hanzala Alam", 'Depart' : "Embedded", 'Section' : "A"}
dict.clear()
print(dict)