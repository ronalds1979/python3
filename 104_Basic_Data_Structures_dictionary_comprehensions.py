#functions to add space lines and traces

def space_lines ():
    return print('')

def space_traces ():
    print('--------------------------------------------------------')

def divider_results():
    space_lines()
    space_traces()
    space_lines()

#Dictionary Comprehensions
print ('Dictionary Comprehensions')
print (
    '''
    Generate dictionaries from iterable structures
    very similar to list comprehensions
    '''
)

print('')
print ('a list of tuples')
animalList = [('a', 'aardvark'),('b', 'bear'), ('c', 'cat'), ('d', 'dog')]
print (animalList)
print('')
print ('create a dictionary from list of tuples using iterations')
animals = {item[0]: item[1] for item in animalList}
print (animals)
print('')
print('a more elegant way to create a dictionary from list of tuples using iterations')
animals = {key: value for key, value in animalList}
print (animals)

print('')
print (animals.keys())
print (animals.values())
print (animals.items())

print('')
print('transform a dictionary in a list')
print (list(animals.items()))

print('')
print('transform a dictionary in a list with different keys')
print ([{'letter': key, 'name': value} for key, value in animals.items()])

divider_results

print('')

print('')
