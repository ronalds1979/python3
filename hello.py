Salutation ='Hello'
Space = ' '
Subject = 'World'
whole_string = (Salutation + ',' + Space + Subject)
print(whole_string)

print(Subject)
print('The first letter of ' + Salutation + ' is ' + Salutation[0] + ', because 0 represents the first letter of the string')

# Iterate through items in a range
for i in range(0, 5):
    print('Number: {}'.format(i))

name = input ('What is your name? ')
thing = input ('What is your favorite activity?')
print ('Miss ' + name + ' favourite activity is ' + thing)