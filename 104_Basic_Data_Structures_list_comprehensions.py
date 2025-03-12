#functions to add space lines and traces

def space_lines ():
    return print('')

def space_traces ():
    print('--------------------------------------------------------')

def divider_results():
    space_lines()
    space_traces()
    space_lines()

#List Comprehensions
print ('List Comprehensions')

myList = [1,2,3,4,5]
print(myList)
print('')
print('Multiplies by 2 each item of list')
print([2*item for item in myList]) #the list comprehension goes inside square brackets []
print('')
print('There is no change on mylist')
print(myList)

divider_results()

#List Comprehensions with filters
print ('List Comprehensions with filters')

print('create a list with content as a range from 0 to 100')
myList = list(range(100))
print('')
print('create a filtered list from the original list using as criteria items that divided per 10 there is no remainder only 0')
filteredList = [item for item in myList if item % 10 == 0]
print (filteredList)
print('')
print ('create a filtered list from the original list using as criteria items that divided per 10 there is a remainder lower than 3')
filteredList = [item for item in myList if item % 10 < 3]
print (filteredList)
divider_results()

#List Comprehensions with functions
print ('List Comprehensions with functions')
print ('')
myString = 'My name is Ronaldo Freitas. I live in Esplugues'
print(myString)
print ('')
print ("split by '.'")
print (myString.split('.'))
print ('')
print ("split by ' '")
print (myString.split())
print ('')
print ("clean string using a function to replace'.' by '' and make string lower case")
def cleanWord(word):
    return word.replace('.', '').lower() # chaining two functions in same line
print('')
print ('call the function cleanWord(word) for each word in mystring.split() that split the text by space')
print ([cleanWord(word) for word in myString.split()])
print('')
print ('call the function cleanWord(word) for each word in mystring.split() that split the text by space for only words smaller than three (3)')
print ([cleanWord(word) for word in myString.split() if len(cleanWord(word)) < 3])



divider_results()

#Nested List Comprehensions 
print ('Nested List Comprehensions')

print('')
print ("call the function cleanWord(word) for each word in sentence.split() that split the text by space from the sentence that was split by '.' before")
print ([[cleanWord(word) for word in sentence.split()] for sentence in myString.split('.')])


divider_results()


