

people = ['John', 'sara', 'susan']


for person in people:
    print(f'Current Person: {person}')



# break 
# stop loop if person is sara 
for person in people:
    if person == 'sara': 
      break 
    print(f'Current Person: {person}')



# continue 
for person in people:
    if person == 'sara': 
      continue 
    print(f'Current Person: {person}')



# range 
for i in range(len(people)): 
  print(f'hello {people[i]}')


for i in range(0, 5): 
  print(f'Number: {i}')


  # while loop 

  count = 0
  while count <= 10: 
    count += 1 
    print(f'count: {count}')