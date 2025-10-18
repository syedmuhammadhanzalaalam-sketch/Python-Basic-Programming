#1 Strings
name = "Syed Hanzala Alam"
university = "University of lahore"
print(name,university)

#2 Access values in String
stringvariable = "Syed Hanzala Alam"
print("stringvariable[0]:", stringvariable[0]) 
print("stringvariable[1:5]:", stringvariable[1:5])

#3 Updating String
stringvariable = "Syed Hanzala"
stringvariable = stringvariable[:7] + "Alam"
print("Updated String:", stringvariable)
#4
stringvariable = "Syed Hanzala Alam"
print(stringvariable)
del stringvariable
print(stringvariable)

#5 String special operators
# '+' operator is used for concatenation.
variable = "Syed Hanzala Alam"
print("Syed Hanzala Alam + python")

# "*" used of Repetition 
variable = "Syed Hanzala Alam"
print(variable*3)

# [] give the character of string at given index.
variable = "Hanzala"
print(variable[0])

#'[:]' is used to get a range of characters from string.
variable = "Hanzala"
print(variable[2:5])

#'in' returns true if given character exists in string, otherwise false.
variable = "Hanzala"
print("f" in variable)

#'in'  returns true if given character doesn't exists in string, otherwise false.
variable = "Hanzala"
print("a" not in variable)

# String formatting operator.
print("My name is %s and my age is %d" % ("Hanzala", 20))