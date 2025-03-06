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

print('''
### Class ###

    In object-oriented programming, a class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects (instances) will have. Classes encapsulate data for the object and provide a way to define behaviors associated with that data.
    Here are the key components of a class:

        Attributes (or Properties): These are variables that hold the data associated with a class. Attributes define the state of an object. They can be instance attributes (specific to an instance of the class) or class attributes (shared across all instances of the class).

            Example:
       ''')


class Dog:
    species = "Canine"  # Class attribute
    
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

print('''
Methods: These are functions defined within a class that describe the behaviors of the objects created from the class. Methods can operate on the attributes of the class and can take parameters.

Example:
       ''')
class Dog:
    def bark(self):
        return "Woof!"

print('''Constructor: This is a special method called __init__ in Python, which is automatically called when a new instance of the class is created. It initializes the attributes of the class.

Example:
      ''')
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

print('''
      Inheritance: This allows a class to inherit attributes and methods from another class, promoting code reuse. The derived class (child class) can extend or override the functionality of the base class (parent class).

Example:
      ''')
class Puppy(Dog):  # Puppy inherits from Dog
    def play(self):
        return "Playing!"

print('''
      Encapsulation: This is the concept of restricting access to certain components of an object. In Python, this is often achieved using private attributes (prefixing with an underscore) to hide them from outside access.

Example:
      ''')
class Dog:
    def __init__(self, name):
        self._name = name  # Protected attribute

print ('''
       Polymorphism: This allows methods in different classes to be defined with the same name but behave differently based on the object that is calling them. This is often used in conjunction with inheritance.

Example:
       ''')
class Cat:
    def sound(self):
        return "Meow!"

class Dog:
    def sound(self):
        return "Woof!"

def make_sound(animal):
    print(animal.sound())

print('''
      In summary, a class in Python is a fundamental concept in object-oriented programming that allows for the creation of reusable and organized code through encapsulation, inheritance, and polymorphism. If you have any further questions or need clarification on any specific aspect of classes, please let me know!
      ''')