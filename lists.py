# a list is a collection which is ordered & changeable. allows duplicate members
# basically like an array in JS


# create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apple', 'Orange', 'grapes', 'pears']


# use a constructor
# similar to new Array in JS
numbers2 = list((1, 2, 3, 4, 5))

# lists are zero based just like arrays in js
# get single value from list
print(fruits[1])


# get length of list
print(len(fruits))


# append to end of list
fruits.append('strawberries')

# remove from list
fruits.remove('grapes')


# insert into specific position
fruits.insert(2, 'banana')


# remove from specific position
fruits.pop(1)


# reverse list
fruits.reverse()


# sort alphabetically
fruits.sort()


# reverse sort alphabetically
fruits.sort(reverse=True)



# change value 
fruits[0] = 'Blueberries'


print(fruits)
