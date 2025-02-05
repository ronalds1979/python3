#functions to add space lines and traces

def space_lines ():
    return print('')

def space_traces ():
    print('-------')

# Lists
print ('Lists')
space_lines
space_traces

# Lists Slicing
print ('Lists Slicing')
space_lines
space_traces

myList = [1,2,3,4,5,6]
print (myList)
print ('Three to the end skip the first three elements and show from 4 until the end')
print (myList[3:]) # Three to the end skip the first three elements and show from 4 until the end

print ('Start from first element 0 using steps of 2 and show from element 0 until the element 3')
print (myList[0:3:2]) # Start from first element 0 using steps of 2 (two is step size) and show from element 0 until the element 3
print (myList[0:6:4]) # Start from first element 0 using steps of 4 (four is step size) and show from element 0 until the element 6
print (myList[::2]) # Start from first element 0 using steps of 2 (two is step size) and show from element 0 in the beginning until the end

space_lines
space_traces

for i in range (15):
    print (i)

mylist = list(range(100))
print (mylist[::10])
print (mylist[::-10])

space_lines
space_traces


# Modifying Lists
print ('Modifying Lists')
space_lines
space_traces

myList = [1,2,3,4]
print (myList)
myList.append(5) #append an element to the end of the list
print (myList)

myList = [1,2,3,4]
print (myList)
myList.insert(1,7) #insert an element (7) at a defined position (1) on the list
print (myList)


space_lines
space_traces


