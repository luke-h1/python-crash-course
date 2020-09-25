# comments
'''
This is a multi line comment 
'''
# this is a single line comment


# variables
'''
 - variable names are case sensitive  
 - must start with a letter or underscore
 - can have numbers but cannot start with one 
 -  no semicolons. 
 - no keyword to define a variable (i.e. const i = 1 )
'''


#booleans 
""" 
# capital T for true 
# capital F for false 
"""

x = 1             # int (whole number)
y = 2.5           # float (decimal point)
name = 'John Doe' # string (text)
isCool = True     # boolean (true + false)

# Multiple assignments 
x, y, name, isCool = (1, 2.5, 'John', True) # similar to destructuring in JS 

print('hello world') # console.log()


# basic math ops 
# the same as JS 
# + = add
# - = minus 
# * = multiply 
# / = division
# % = modulus 

# casting 
x = str(x) 
print(type(x)) # str 

y = int(y)
print(type(y)) # int. 
