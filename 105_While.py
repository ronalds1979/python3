# Class to help to organize the output and document the code
class Toolbox:
    def addTripleLineSeparator():
        print('')
        print ('----------------------------------------------------------------------')
        print('')
    def addSingleLineSeparator():
        print('')


Toolbox.addTripleLineSeparator()

print ('### While ###')

Toolbox.addSingleLineSeparator()

from datetime import datetime

print (datetime.now().hour)
print (datetime.now().minute)
print (datetime.now().second)

Toolbox.addSingleLineSeparator()
print ('wait 5 seconds logic (pass)')
Toolbox.addSingleLineSeparator()
print (f'We are at {datetime.now().second} seconds')
print ('wait for 5 seconds')
wait_until = (datetime.now().second + 5)
if wait_until > 59:
    wait_until = wait_until - 60
while datetime.now().second != wait_until:
    #print('Still waiting')
    pass
print (f'We are at {wait_until} seconds')

Toolbox.addTripleLineSeparator()

print ('wait 5 seconds logic (break)')
Toolbox.addSingleLineSeparator()
print (f'We are at {datetime.now().second} seconds')
print ('wait for 5 seconds')
wait_until = (datetime.now().second + 5)
if wait_until > 59:
    wait_until = wait_until - 60
while True:
    if datetime.now().second == wait_until:
        print (f'We are at {wait_until} seconds')
        break

Toolbox.addSingleLineSeparator()

print ('wait 5 seconds logic (continue)')
Toolbox.addSingleLineSeparator()
print (f'We are at {datetime.now().second} seconds')
print ('wait for 5 seconds')
wait_until = (datetime.now().second + 5)
if wait_until > 59:
    wait_until = wait_until - 60
while datetime.now().second != wait_until:
    continue
    print('Still waiting')
    #pass
print (f'We are at {wait_until} seconds')