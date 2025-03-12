# Class to help to organize the output and document the code
class Toolbox:
    def addTripleLineSeparator():
        sep = ('__ . _ . __       ')
        print('')
        print (sep)
        print('')

    def addSingleLineSeparator():
        print('')


Toolbox.addTripleLineSeparator()

print ('### The anatomy of a class ###')

Toolbox.addSingleLineSeparator()

class Dog:
    def __init__(self, name):
        self.name = name # instance attribute name
        self.legs = 4 # instance attribute legs
    
    def speak(self):
        print(self.name + ' says: Bark!')
        return 'ok'

Toolbox.addSingleLineSeparator()

my_dog = Dog('Rex')
print ('The dog name is ' + my_dog.name)                                    # print instance attribute name
print ('The dog ' + my_dog.name + ' has ' + str(my_dog.legs) + ' legs')     # print instance attribute name and legs
print (my_dog.speak())                                                      # use method speak
print (Dog('Rex1').speak())

Toolbox.addSingleLineSeparator()

class Dog1:
    _legs = 4 # legs is now a static attribute not instance attribute anymore. This will not change with each instance, it is not dynamic, it is static
    # _ underline is a warning to not change the class static attribute that can break things
    # these private details are implementation details
    
    def __init__(self, name):
        self.name = name # instance attribute name
        
    def getLegs(self):
        return self._legs

    def speak(self):
        print(self.name + ' says: Bark!')
        return 'ok'

Toolbox.addSingleLineSeparator()

myDog = Dog1('Xer') # self will be my_dog
print ('The dog name is ' + myDog.name)                                    # print instance attribute name
print ('The dog ' + myDog.name + ' has ' + str(myDog.getLegs()) + ' legs')     # print instance attribute name and legs
print (my_dog.speak())                                                      # use method speak
print (Dog1('Xer1').speak())

Toolbox.addSingleLineSeparator()


myDog = Dog1('Xer') # self will be my_dog
myDog._legs = 3 # change the instance attribute
print ('The dog name is ' + myDog.name)                                    # print instance attribute name
print ('The dog ' + myDog.name + ' has ' + str(myDog.getLegs()) + ' legs')     # print instance attribute name and legs
print (my_dog.speak())                                                      # use method speak
print (Dog1('Xer1').speak())

Toolbox.addSingleLineSeparator()

