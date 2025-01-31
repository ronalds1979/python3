#functions to add space lines and traces

def space_lines ():
    return print('')

def space_traces ():
    print('-------')

import math

print ('Strings')
space_lines()
print ('Slicing')
space_lines()
name = 'My name is Ronaldo'
#name = '0123456789123'
print (name)
print ('The first letter of string is ' + str(name[0]))
print ('The second letter of string is ' + str(name[1]))
print ('The first six letters of string are ' + str(name[0:7]))
print ('The first six letters of string are ' + str(name[:7]))
print ('The last letters of string starting at 12 are ' + str(name[11:]))

space_lines()
print ('Formating')
space_lines()

print ('my number is ' + str(5))
print (f'my number is {5}') #use a value
print (f'my number is {5} and twice that is {2*5}') #use a arithmetic operation
print (f'Pi is {math.pi}') #call a function
print (f'Pi is {math.pi:.2f}') #call a function and format to 2 decimals
print('Pi is: {}' .format(math.pi)) #old format before Python version 3.6
print(f'string followed by a int, in this case 5 {5}')
print(f'string followed by a string, in this case text = {'text'}')
print(f'string followed by a float, in this case 1.14 = {1.14}')
print(f'string followed by a arithmetic operation, in this case 9/5 = {9 / 5}')
print(f'string followed by a arithmetic operation, in this case 9*5 = {9 * 5}')
print(f'string followed by a arithmetic operation, in this case 2 ** 3 = {2 ** 3}')
print(f'string followed by a function, in this case str(5) {str(5)}')

space_lines()
print ('Formating')
space_lines()

print (
    '''
Here is my long block of text
I can add new lines!
the text does not stop until it see \'\'\'
'''
)