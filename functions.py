# in python you do not use curly brackets, use indentation with tabs or spaces


# create a function & set a default value if nothing is passed in

def sayHello(name='default'):
    print('hello', name)


# call the function. Again very similar to js
sayHello('luke')


# return values
def getSum(num1, num2):
    total = num1 + num2
    return print(total)


getSum(4, 4)


# a lambda function is a small anonymous function
# a lambda function can take any numbers of arguments, but you can only have one express. very similar to js arrow functions
# implicity returns val 

getSum = lambda num1, num2 : num1 + num2 



print(getSum(10, 10))