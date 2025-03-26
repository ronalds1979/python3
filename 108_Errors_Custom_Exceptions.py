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
print('### Custom exceptions ###')

Toolbox.addTripleLineSeparator()

# Define a custom exception class that inherits from Exception
class CustomException(Exception):
    pass  # No additional functionality; it just serves as a unique exception type

# Function that raises the CustomException with a message
def causeError():
    raise CustomException('You called the causeError function!')  # Raise the custom exception

causeError()  # Call the function to demonstrate raising the exception

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

# Print the title of the code anatomy again
print('### Custom exceptions ###')

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

# Define a base class for HTTP exceptions, inheriting from Exception
class HttpException(Exception):
    statusCode = None  # Initialize status code to None
    message = None  # Initialize message to None

    # Constructor to initialize the exception with a status code and message
    def __init__(self):
        super().__init__(f'Status code: {self.statusCode} and message is {self.message}')

# Define a NotFound exception that inherits from HttpException
class NotFound(HttpException):
    statusCode = 404  # Set the status code for NotFound
    message = 'Resource not found!'  # Set the message for NotFound

# Define a ServerError exception that inherits from HttpException
class ServerError(HttpException):
    statusCode = 500  # Set the status code for ServerError
    message = 'The server messed up!'  # Set the message for ServerError

# Function that raises a ServerError
def raiseServerError():
    raise ServerError()  # Raise the ServerError

raiseServerError()  # Call the function to demonstrate raising the ServerError

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

