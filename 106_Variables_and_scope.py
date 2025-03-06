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
