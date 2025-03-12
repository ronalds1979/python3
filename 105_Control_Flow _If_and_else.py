# Class to help to organize the output and document the code
class Toolbox:
    def addTripleLineSeparator():
        print('')
        print ('----------------------------------------------------------------------')
        print('')
    def addSingleLineSeparator():
        print('')


Toolbox.addTripleLineSeparator()

print ('### If and else ###')

Toolbox.addSingleLineSeparator()

print ('### elif ###')

Toolbox.addSingleLineSeparator()
# For a range 1-100 check each item for different conditions, in case the condition match returns a string otherwise the number itself
print('Problem statement: Find the divider for numbers 1-100 following these rules: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, FizzBuzz, 16 ')
for item in range (1,101):
    if item % 15 == 0:
        print ('Fizzbuzz')
    elif item % 5 == 0: # covers 5 and 10
        print ('Buzz')
    elif item % 3 == 0: # covers 3, 6, 9, 12
        print ('Fizz')
    else:
        print(item)
    if item % 2 == 0:
        print ('It is even!')
Toolbox.addTripleLineSeparator()


Toolbox.addSingleLineSeparator()
# For a range 1-100 check each item for different conditions, in case the condition match returns a string otherwise the number itself
for item in range (1,101):
    print('Fizzbuz' if item % 15 == 0 else 'Buzz' if item % 5 == 0 else 'Fizz' if item % 3 == 0 else item)
Toolbox.addTripleLineSeparator()


Toolbox.addSingleLineSeparator()
# For a range 1-100 check each item for different conditions, in case the condition match returns a string otherwise the number itself returns a list
print(['Fizzbuz' if item % 15 == 0 else 'Buzz' if item % 5 == 0 else 'Fizz' if item % 3 == 0 else item for item in range (1,101)])
Toolbox.addTripleLineSeparator()