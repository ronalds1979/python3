# Class to help organize the output and document the code
class Toolbox:

    # Method to print a triple line separator for visual clarity
    def addTripleLineSeparator():
        sep = ('__ . _ . __       ')  # Define the separator string
        print('')  # Print a blank line for spacing
        print(sep)  # Print the separator
        print('')  # Print another blank line for spacing

    # Method to print a single line separator for visual clarity
    def addSingleLineSeparator():
        print('')  # Print a blank line for spacing

# Add a triple line separator at the beginning of the output
Toolbox.addTripleLineSeparator()

# Print the title of the code anatomy
print('### The anatomy of a class ###')

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

# Class representing a Dog
class Dog:

    # Constructor to initialize the Dog object with a name
    def __init__(self, name):
        self.name = name  # Instance attribute to store the dog's name
        self.legs = 4  # Instance attribute to store the number of legs (default is 4)

    # Method for the dog to "speak"
    def speak(self):
        print(self.name + ' says: Bark!')  # Print the dog's name and its sound
        return 'ok'  # Return a confirmation string

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

# Create an instance of Dog with the name 'Rex'
my_dog = Dog('Rex')

# Print the dog's name
print('The dog name is ' + my_dog.name)  # Access and print the instance attribute name

# Print the dog's name and the number of legs
print('The dog ' + my_dog.name + ' has ' + str(my_dog.legs) + ' legs')  # Access and print instance attributes

# Call the speak method of my_dog and print the result
print(my_dog.speak())  # Use the method speak

# Create another Dog instance and call speak directly
print(Dog('Rex1').speak())  # Demonstrate creating a new instance and calling speak

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

# Class representing a Dog with a static attribute for legs
class Dog1:
    _legs = 4  # Static attribute for legs; shared across all instances

    # The underscore indicates that this attribute should not be modified directly
    # These private details are implementation details

    # Constructor to initialize the Dog1 object with a name
    def __init__(self, name):
        self.name = name  # Instance attribute to store the dog's name

    # Method to get the number of legs (static)
    def getLegs(self):
        return self._legs  # Return the static attribute _legs

    # Method for the dog to "speak"
    def speak(self):
        print(self.name + ' says: Bark!')  # Print the dog's name and its sound
        return 'ok'  # Return a confirmation string

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

# Create an instance of Dog1 with the name 'Xer'
myDog = Dog1('Xer')  # self will refer to myDog

# Print the dog's name
print('The dog name is ' + myDog.name)  # Print the instance attribute name

# Print the dog's name and the number of legs using getLegs method
print('The dog ' + myDog.name + ' has ' + str(myDog.getLegs()) + ' legs')  # Access and print instance attributes

# Call the speak method of myDog and print the result
print(myDog.speak())  # Use the method speak

# Create another Dog1 instance and call speak directly
print(Dog1('Xer1').speak())  # Demonstrate creating a new instance and calling speak

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

# Create another instance of Dog1
myDog = Dog1('Xer')  # self will refer to myDog

# Attempt to change the static attribute _legs (not recommended)
myDog._legs = 3  # Change the instance attribute (note: this does not change the static value)

# Print the dog's name
print('The dog name is ' + myDog.name)  # Print the instance attribute name

# Print the dog's name and the number of legs using getLegs method
print('The dog ' + myDog.name + ' has ' + str(myDog.getLegs()) + ' legs')  # Access and print instance attributes

# Call the speak method of myDog and print the result
print(myDog.speak())  # Use the method speak

# Create another Dog1 instance and call speak directly
print(Dog1('Xer1').speak())  # Demonstrate creating a new instance and calling speak

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()