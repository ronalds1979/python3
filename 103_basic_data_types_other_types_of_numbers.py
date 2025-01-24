#functions to add space lines and traces

def space_lines ():
    return print('')

def space_traces ():
    print('-------')

# class and function import for decimal numbers
from decimal import Decimal, getcontext

# Other types of numbers

print ('convert string to int with a base number. e.g base 2, base 16, etc. it always required the argument as string')
space_lines()
print ('100 is equal to ' + str(int('100',2)) + " in base 2. int('100',2)")
print ('1ab is equal to ' + str(int('1ab',16)) + " in base 16. int('1ab',16)")

space_lines()
print ('working with decimal to cover float limitations')
space_lines()
print ('Function getcontext() returns global settings that get applied ')
space_lines()
print (getcontext())
space_lines()
print('change glabal settings for the function')
getcontext().prec=2
print('Decimal function requires and argument as string to work')
print("Decimal ('1') / Decimal ('3') is equal to " + str(((Decimal ('1') / Decimal ('3')))))
print("Decimal(3.14) is equal to " + str(Decimal(3.14)))
print("Decimal('3.14') is equal to " + str(Decimal('3.14')))
space_lines()
space_traces()
space_lines()
print ('Always round the numbers before return to user')
space_lines()
space_traces()
space_lines()