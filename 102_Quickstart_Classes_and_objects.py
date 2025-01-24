#functions to add space lines and traces

def space_lines ():
    return print('')

def space_traces ():
    print('-------')

# Classes and objects
print ('Classes and objects')
print ('Classes name start with uppercase letter')

space_lines
space_traces
space_lines

class Dog:
    # __init__ function is a special one, stand for initialization. It is called whenever an instance of the class Dog is created
    # the variable self is the specific instance of the Dog class after we have initialized it
    # self represent the instances of the class. These classes instances are the objects.
    # the variable inside the class are the attributes of the objects
    # the functions inside the class are the methods. The dog object has the method speak

    def __init__(self, name):
        self.name = name
        self.legs = 4
    def speak(self):
        print(self.name +' says: Bark!')

# use the class

my_dog = Dog('Rover')
another_dog = Dog('Fluffy')

my_dog.speak()
another_dog.speak()



