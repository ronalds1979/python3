#functions to add space lines and traces

def space_lines ():
    return print('')

def space_traces ():
    print('-------')

# Booleans
print ('Numbers')

space_lines()

print (bool(1))
print (bool(100))
print (bool(-1))
print (bool(0))
print (bool(0.0))
print (bool(0j))
print (bool(1j))

space_lines()

print('Strings')

space_lines()

print (bool('True'))
print (bool('False'))
print (bool(' '))
print (bool(''))
print (bool(1))
print (bool(1))

space_lines()

print('Data structures')

space_lines()

print (bool([]))
print (bool({}))
print (bool(()))
print (bool([1]))

space_lines()

print('None')

space_lines()

print (bool(None))

space_lines()

print('Boolean logic')

space_lines()

wheatherIsNice = False
haveUmbrella = True

if not (haveUmbrella or wheatherIsNice):
    print('Stay inside')
else:
    print('Go for a walk')

if (not haveUmbrella) and (not wheatherIsNice):
    print('Stay inside')
else:
    print('Go for a walk')

if haveUmbrella or wheatherIsNice:
    print('Go for a walk')
else:
    print('Stay inside')
