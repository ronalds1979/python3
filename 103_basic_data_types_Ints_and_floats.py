#functions to add space lines and traces

def space_lines ():
    return print('')

def space_traces ():
    print('-------')

# Ints adn floats

print ('These operations always return a float')
print (20 / 4)
print (4 + 4.0)
print (4 * 4.0)
print (4 ** 4.0)

space_lines()
space_traces()
space_lines()

print ('Casting is the action to convert from float to int like example int(4 ** 4.0)')
print (int(4 ** 4.0))
space_lines()
print ('some issues with casting from float to int because it converts float to int but it does not round. 8.999 became...')
print (int (8.999))
print ('to round a float we should use round function')
print (round(8.999))
space_lines()
print (int(14/3))
print (round(14/3))
print ('to round a float we should use round function and we can add number of decimals like 2')
print (round(8.999, 2))
space_lines()
print (int(14/3))
print (round(14/3,2))
space_lines()
print ('example with three cases')
print ('int(14/3) is equal ' + str(int(14/3)))
print ('round(14/3) is equal ' + str(round(14/3)))
print ('round(14/3, 2) is equal ' + str(round(14/3, 2)))
space_lines()
print('one of the pitfalls with float. They are aproximations')
print ('1.2 - 1.0 is equal to ' + str(1.2 - 1.0))
print ('round function can help. round(1.2 - 1.0) is equal to ' + str(round(1.2 - 1.0, 2)))