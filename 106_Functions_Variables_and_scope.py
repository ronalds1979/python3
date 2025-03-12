# Class to help to organize the output and document the code
class Toolbox:
    def addTripleLineSeparator():
        sep = ('__ . _ . __       ')
        print('')
        print (sep)
        print('')

    def addSingleLineSeparator():
        print('')


Toolbox.addTripleLineSeparator()

print ('### Variables and scope ###')

Toolbox.addSingleLineSeparator()

def performOperation(num1, num2, operation='sum'):
    print('locals(): variables available locally inside the function')
    print(locals())

performOperation(1,2, operation='multiply')

Toolbox.addTripleLineSeparator()

print ('Global variables are defined outside the function in the main body of the code')
print(globals())

Toolbox.addTripleLineSeparator()

Toolbox.addSingleLineSeparator()

print ('Global and Local Scope')
message = 'Some global data'
varA = 2
def function1(varA, varB):
    print ('varA local scope')
    print(varA)
    print (message)
    print(locals())

def function2(varC, varB):
    print ('varA global scope')
    print(varA)
    print (message)
    print(locals())

function1(1,2)
function2(3,4)

Toolbox.addSingleLineSeparator()
Toolbox.addSingleLineSeparator()

def function1(varA, varB):
    message = 'Some local data'
    print (varA)
    def inner_function(varA, varB):
        print(f'inner_function local scope: {locals()}')
    inner_function(123,456)

function1(1,2)

Toolbox.addSingleLineSeparator()
Toolbox.addSingleLineSeparator()

def function1(varA, varB):
    message = 'Some local data'
    print (varA)
    def inner_function(varA, varB):
        print(f'inner_function local scope: {locals()}')
    print(locals())
    inner_function(123,456)

function1(1,2)