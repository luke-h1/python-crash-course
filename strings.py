
name = 'Luke'
age = 21


# concat 

# very similar to javascript 
print('hello, my name is ' + name + ' & I am ' + str(age))

# args by position
# much cleaner than the above
print('My Name is {name} & I am {age}'.format(name=name, age=age))






# string formatting
'''
str() = convert something to a string 


'''


# string methods 

s = 'hello world'

# capitalize string
print(s.capitalize())


# make all uppercase 
print(s.upper())

# make all lower 
print(s.lower())

# get length
print(len(s))


# replace 
print(s.replace('world', 'everyone'))


# turn into a list (list is an array)
print(s.split()) 