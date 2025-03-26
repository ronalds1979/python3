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
print('### Errors and exceptions ###')

Toolbox.addTripleLineSeparator()

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

def causeError ():
    return 1/0

causeError()

Toolbox.addSingleLineSeparator()


def causeError1 ():
    try:
        return 1/0
    except Exception as e:
        #print (type(e))
        return e

causeError1()