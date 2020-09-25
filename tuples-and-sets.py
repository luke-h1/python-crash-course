# a tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# cannot modify values


# single value needs trailing comma
#  fruits3 = ('Apples', )

# create a tuple

fruits = ('Apples', 'Pears', 'Oranges')


print(fruits)

# constructor
fruits2 = tuple(('apples', 'pears', 'oranges'))


# get value from tuple
print(fruits[0])


# delete tuple
del fruits2


# a set is a collection which is unordered and unindexed. no duplicate members


# create set


fruits_set = {'Apple', 'Orange', 'blueberries'}


# check if in set

print('Apple' in fruits_set)  # this returns either a true or a false value


# add to set
fruits_set.add('Hello')


# remove from set
fruits_set.remove('Orange')


# clear set entirely
fruits_set.clear()


# delete set

del fruits_set
