# Class to help to organize the output and document the code
class Toolbox:
    def addTripleLineSeparator():
        print('')
        print ('----------------------------------------------------------------------')
        print('')
    def addSingleLineSeparator():
        print('')


Toolbox.addTripleLineSeparator()

print ('### For ###')

Toolbox.addSingleLineSeparator()

myList = [1,2,3,4]
for item in myList:
    print(item)

Toolbox.addSingleLineSeparator()

print ('### For with Pass ###')

Toolbox.addSingleLineSeparator()

animalLookup =  {
    'a' : ['aardvark','antelope'],
    'b' : ['bear'],
    'c' : ['cat'],
    'd' : ['dog'],
}
for letter, animals in animalLookup.items():
    pass

Toolbox.addSingleLineSeparator()
print ('### For with Continue ###')
print(animalLookup)
print ('print only if the animal item has one entry, if it has more continue and skip the item')
for letter, animals in animalLookup.items():
    if len(animals) > 1:
        continue
    print (f'Only one animal on {letter} equal to {animals}')

Toolbox.addSingleLineSeparator()
print ('### For with Break ###')
print(animalLookup)
print ('print only if the animal item has more than one entry, if it has less continue and skip the item')
for letter, animals in animalLookup.items():
    if len(animals) > 1:
        print (f'Found on {letter} equal to {len(animals)} animals {animals}')
        break # it will stop the code after the first item found with the condition
    
Toolbox.addSingleLineSeparator()
print ('### For / Else ###')
print('find out all the primes between 2 and 100')
for number in range(2,100): # range between 2 and 100, get number
    for factor in range(2, int(number**0.5) +1): # calculate the factor of number and iterate through it number**0.5 is the same of square root of the number
        if number % factor == 0: # test each number, divide number by factor, if the number divided the factor (square root of the number) with remain 0 it is not prime
            break
    else:
        print(f'{number} is prime!')