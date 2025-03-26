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
print('### Bad Arguments ###')

Toolbox.addTripleLineSeparator()

# Define a custom exception for non-integer arguments
class NonIntArgumentException(Exception):
    print ('There is no Int in one of the arguments. Please review the arguments provided')
    pass  # Inherits from Exception; no additional functionality

# Decorator function to handle non-integer arguments for a given function
def handleNonIntArguments(func):
    def wrapper(*args):  # Inner wrapper function that takes any number of arguments
        for item in args:  # Iterate over the arguments
            if type(item) is not int:  # Check if the argument is not an integer
                raise NonIntArgumentException()  # Raise the custom exception if a non-int is found
        return func(*args)  # Call the original function with the validated arguments
    return wrapper  # Return the wrapper function

# Decorate the sum function to enforce integer arguments
# Decorators take in arguments and can do anything they want with them before passing to the function.
# Decorators can run code before and after executing a function, which is great for setup and teardown.
# Decorators can get the returned values of a function and modify them before returning to the caller.
# Decorators cannot Change the name of a function.

@handleNonIntArguments
def sum(a, b, c):
    return a + b + c  # Return the sum of the three arguments

# Try to call the sum function with invalid arguments
try:
    result = sum(1, 2, 'a')  # This should raise an exception
    print('This should not print out')  # This line should not execute
except NonIntArgumentException as e:  # Catch the custom exception
    print('Hooray! The exception was raised')  # Print a success message indicating the exception was raised