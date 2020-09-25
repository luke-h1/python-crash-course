x = 5
y = 11

# # comparison ops & if else
# if x > y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{x} is not greater than {y}')


# elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to  {y}')
else:
    print(f'{x} is not greter than {y}')


# Nested if statements

if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10 ')


# logical ops (and, or , not )

if x > 2 and x <= 10:  # both have to be true
    print(f'{x} is greater than 2 and less than or equal to 10 ')


if x > 2 or x <= 10:  # only one has to be true
    print(f'{x} is greater than 2 and less than or equal to 10 ')

if not(x == y):
    print('x is not equal to y')
elif(x > y):
    print('x is greater than  y')


# membership ops (not, not in )


# in
numbers = [1, 2, 3, 4, 5]
if x in numbers:
    print(x in numbers)  # true or false


# not in
if x not in numbers:
    print(x not in numbers)


# is
if x is y:
    print(f'{x} is  {y}')


# is not
if x is not y:
    print(f'{x} is not {y}')
