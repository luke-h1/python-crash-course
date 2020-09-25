# a dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# similar to an object literal in JS


# create dictionary
person = {
    'firstName': 'john',
    'lastName': 'Doe',
    'age': 30
}
print(person)


# get single value
print(person['firstName'])
print(person.get('age'))


# add key value pair
person['phone'] = '555-555-5555'

print(person.get('phone'))


# get all keys
print(person.keys())


# get all items
print(person.items())


# copy a dict
person2 = person.copy()
# similar to spread op in JS
person2['city'] = 'Boston'
print(person2)


# remove item
del (person['age'])
print(person)


# pop item
person.pop('phone')
print(person)


# clear dict
person.clear()
print(person)


# get length
print(len(person2))


# list of dicts
# similar to array of objects


people = [
    {'name': 'bob', 'age': '33'},
    {'name': 'john', 'age': '25'},
]

print(people)

print(people[1]['name'])