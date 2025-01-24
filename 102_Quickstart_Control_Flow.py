#functions to add space lines and traces

def space_lines ():
    return print('')

def space_traces ():
    print('-------')



print ('Control Flow')
print('If / Else statements')
a = True
if a:
    print ('it is true!')
else:
    print('it is false!')
print ('Always print this')

space_lines()
space_traces()
space_lines()

print('Nested if')
a=True
b=True
c=True
if a:
    print('A is True')
    if b:
        print('a and b are true')
        if c:
            print('all three are true')
else:
    print('a is false')
print('always print this')

space_lines()
space_traces()
space_lines()

print('For loops')
a = [1,2,3,4,5]
for item in a:
    print (item)

space_lines()
space_traces()
space_lines()

a = [1,2,3,4,5]
for number in a:
    print (number)
    
space_lines()
space_traces()
space_lines()

print('While loops')
a = 0
while a < 5:
    print(a)
    a = a + 1

space_lines()
space_traces()
space_lines()