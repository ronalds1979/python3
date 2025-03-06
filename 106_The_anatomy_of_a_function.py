import math

# Class to help to organize the output and document the code
class Toolbox:
    def addTripleLineSeparator():
        sep = 7*('__ . _ . __       ')
        print('')
        print (sep)
        print('')

    def addSingleLineSeparator():
        print('')


Toolbox.addTripleLineSeparator()

print ('### The anatomy of a function ###')

def performOperation (num1, num2, operation): # a function with 3 parameters
    if operation == 'sum':
        print (num1 + num2)
    if operation == 'multiply':
        print (num1 * num2)

performOperation(10,20,'sum')
performOperation(10,20,'multiply')

Toolbox.addTripleLineSeparator()

print ('### Named Parameters ###')
Toolbox.addSingleLineSeparator()
print ('Rules')
print ('Keywords arguments must come after positional arguments')
print('Afterwards, keyword arguments can be in any order')
Toolbox.addSingleLineSeparator()
def performOperation (num1, num2, operation='sum', message='Default message'): # a function with 3 parameters sum is the default operation
    print (message)
    if operation == 'sum':
        print (num1 + num2)
    if operation == 'multiply':
        print (num1 * num2)
performOperation(10,20)
performOperation(10,20,'sum')
performOperation(10,20,'multiply')
performOperation(10,20,operation='multiply')
performOperation(10,20,message='new message', operation='multiply')

Toolbox.addSingleLineSeparator()

Toolbox.addTripleLineSeparator()

print ('### args ###')
Toolbox.addSingleLineSeparator()

Toolbox.addSingleLineSeparator()

def performOperation (*args): 
    print (args)
        
performOperation(10,20)

Toolbox.addTripleLineSeparator()

print ('### kwargs ###')
Toolbox.addSingleLineSeparator()

Toolbox.addSingleLineSeparator()

def performOperation (*args, **kwargs): # a function with 3 parameters sum is the default operation
    print ('args')
    print (args)
    print ('kwargs')
    print (kwargs)
performOperation(10,20, operation='sum')

Toolbox.addTripleLineSeparator()


print ('### kwargs ###')
Toolbox.addSingleLineSeparator()

Toolbox.addSingleLineSeparator()
import math
def performOperation (*args, operation='sum', message='Default message'): # a function with 3 parameters sum is the default operation
    print ('')
    print (f'There are {len(args)} arguments which are: {args}')
    print (message)
    if operation == 'sum':
        return sum(args)
    if operation == 'multiply':
        pass
        return math.prod(args)
print (performOperation(10,20))
print (performOperation(10,20,operation='multiply'))
print (performOperation(1,2,3,4,5,6,7,8, operation='sum'))
print (performOperation(1,2,3,4,5,6,7,8))
print (performOperation(1,2,3,4,5,6,7,8,operation='multiply'))
print (performOperation(1,2,3,4,5,6,7,8,operation='sum'))
print (performOperation(1,2,3,4,5,6,7,8,operation='multiply',message='multiplying'))
print (performOperation(1,2,3,4,5,6,7,8,operation='sum',message='sum'))

Toolbox.addTripleLineSeparator()