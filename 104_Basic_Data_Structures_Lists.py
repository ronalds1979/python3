#functions to add space lines and traces

def space_lines ():
    return print('')

def space_traces ():
    print('--------------------------------------------------------')

# Lists
print ('Lists')
space_lines
space_traces

# Lists Slicing
print ('Lists Slicing')
space_lines()
space_traces()

myList = [1,2,3,4,5,6]
print (myList)
print ('Three to the end skip the first three elements and show from 4 until the end')
print (myList[3:]) # Three to the end skip the first three elements and show from 4 until the end

print ('Start from first element 0 using steps of 2 and show from element 0 until the element 3')
print (myList[0:3:2]) # Start from first element 0 using steps of 2 (two is step size) and show from element 0 until the element 3
print (myList[0:6:4]) # Start from first element 0 using steps of 4 (four is step size) and show from element 0 until the element 6
print (myList[::2]) # Start from first element 0 using steps of 2 (two is step size) and show from element 0 in the beginning until the end

space_lines()
space_traces()

for i in range (15):
    print (i) # print 0 to 14 (range of 15) because it starts on zero

mylist = list(range(101))
print (mylist[::10]) # print the list in increment of 10 starting at 0. 0, 10, 20, 30...
print (mylist[::-10]) # print the list as countdown starting at 100 event range is 101, in a reduction of 10. 100, 90, 80...

space_lines()
space_traces()


# Modifying Lists
print ('Modifying Lists')
space_lines()
space_traces()

myList = [1,2,3,4]
print (myList)
myList.append(5) #append an element to the end of the list
print (myList)

# insert a line in any position
print ('insert 7 to position 1 in the list')
myList = [1,2,3,4]
print (myList)
myList.insert(1,7) #insert an element (7) at a defined position (1) on the list
print (myList)

space_lines()
space_traces()

#remove a item from the list using remove
print ('Remove 7 from mylist using remove')
myList.remove(7)
print(myList)

space_lines()
space_traces()

#remove a item from the list using pop
print ('Remove a item from the end of mylist using pop')
print('The item ' + str(myList.pop()) + ' was removed from the list')
print(myList)

space_lines()
space_traces()

#using while and pop to make a countdown from a list
print ('using while and pop to make a countdown from a list')
while len(myList):
    #print (len(myList))
    print(myList.pop())
print (myList)

space_lines()
space_traces()

print ('modify a variable also modifies a variable that is equals it')
a = [1,2,3,4,5]
b=a
print ('a is equal to ' + str(a))
print ('b is equal to ' + str(b))
print ('append a new value to a (6)')
a.append(6)
print ('a is equal to ' + str(a))
print ('b is equal to ' + str(b))

space_lines()
space_traces()

print ('to avoid that modify a variable also modifies a variable that is equals it we can use copy function')
a = [1,2,3,4,5]
b=a.copy()
print ('a is equal to ' + str(a))
print ('b is equal to ' + str(b))
print ('append a new value to a (6)')
a.append(6)
print ('a is equal to ' + str(a))
print ('b is equal to ' + str(b))

