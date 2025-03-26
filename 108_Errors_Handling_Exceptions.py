import time  # Import the time module to use for timing operations

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
print('### Handling exceptions ###')

Toolbox.addTripleLineSeparator()

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

# Function that causes a division by zero error
def causeError():
    try:
        return 1 / 0  # Attempt to divide by zero
    except Exception as e:  # Catch any exception
        # print(type(e))  # Uncomment to print the type of the exception
        return e  # Return the exception object

causeError()  # Call the function to demonstrate error handling

Toolbox.addSingleLineSeparator()

# Function that handles division by zero and prints a custom error message
def causeErrorCustom():
    try:
        return 1 / 0  # Attempt to divide by zero
    except Exception:  # Catch any exception
        print('Except: Custom error: There was some sort of error')  # Print custom error message

causeErrorCustom()  # Call the function

Toolbox.addSingleLineSeparator()

# Function that handles division by zero and ensures a final message is printed
def causeErrorCustomFinally():
    try:
        return 1 / 0  # Attempt to divide by zero
    except Exception:  # Catch any exception
        print('Except: Custom error: There was some sort of error')  # Print custom error message
    finally:
        print('Finally: This will always execute')  # This message will always be printed

causeErrorCustomFinally()  # Call the function

Toolbox.addSingleLineSeparator()

# Function demonstrating timing and error handling with a finally block
def causeErrorCustomFinally():
    start = time.time()  # Record the start time

    try:
        time.sleep(0.5)  # Simulate a delay
        return 1 / 0  # Attempt to divide by zero
    except Exception:  # Catch any exception
        print('Except: Custom error: There was some sort of error')  # Print custom error message
    finally:
        print(f'Finally: This will always execute. Function took {time.time() - start} seconds to execute!')  # Print execution time

causeErrorCustomFinally()  # Call the function

Toolbox.addSingleLineSeparator()

# Function demonstrating specific exception handling
def causeErrorCustomFinally():
    start = time.time()  # Record the start time

    try:
        time.sleep(0.5)  # Simulate a delay
        return 1 / 0  # Attempt to divide by zero
    except TypeError:  # Catch TypeError specifically
        print('There is a type error')  # Print specific error message
    except ZeroDivisionError:  # Catch ZeroDivisionError specifically
        print('There was a zero division error')  # Print specific error message
    except Exception:  # Catch any other exception
        print('Except: Custom error: There was some sort of error')  # Print custom error message
    finally:
        print(f'Finally: This will always execute. Function took {time.time() - start} seconds to execute!')  # Print execution time

causeErrorCustomFinally()  # Call the function

Toolbox.addSingleLineSeparator()

# Function demonstrating error handling for a TypeError
def causeErrorCustomFinally():
    start = time.time()  # Record the start time

    try:
        time.sleep(0.5)  # Simulate a delay
        return 1 / 'a'  # Attempt to divide by a string, causing TypeError
    except TypeError:  # Catch TypeError specifically
        print('There is a type error')  # Print specific error message
    except ZeroDivisionError:  # Catch ZeroDivisionError specifically
        print('There was a zero division error')  # Print specific error message
    except Exception:  # Catch any other exception
        print('Except: Custom error: There was some sort of error')  # Print custom error message
    finally:
        print(f'Finally: This will always execute. Function took {time.time() - start} seconds to execute!')  # Print execution time

causeErrorCustomFinally()  # Call the function

Toolbox.addSingleLineSeparator()

print('last')  # Print 'last' to indicate the end of the output

# Decorator function to handle exceptions for other functions
def handleException(func):
    def wrapper(*args):  # Define a wrapper function
        try:
            func(*args)  # Call the original function
        except TypeError:  # Catch TypeError specifically
            print('There was a type error')  # Print specific error message
        except ZeroDivisionError:  # Catch ZeroDivisionError specifically
            print('There was a zero division error')  # Print specific error message
        except Exception:  # Catch any other exception
            print('Except: Custom error: There was some sort of error')  # Print custom error message
    return wrapper  # Return the wrapper function

@handleException  # Apply the decorator to the function
def causeError():
    return 1 / 0  # Attempt to divide by zero

causeError()  # Call the decorated function

@handleException  # Apply the decorator to another function
def raiseError(n):
    if n == 0:  # Check if n is zero
        raise Exception()  # Raise a generic exception
    print(n)  # Print the value of n

raiseError(0)  # Call the function with 0, which will raise an exception
raiseError(1)  # Call the function with 1, which will print the value