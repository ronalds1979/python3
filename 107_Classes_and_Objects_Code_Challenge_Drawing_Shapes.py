# Class to help organize the output and document the code
class Toolbox:

    # Method to print a triple line separator for visual clarity
    def addTripleLineSeparator():
        sep = ('__ . _ . __       __ . _ . __       __ . _ . __       ')
        print('')  # Print a blank line
        print(sep)  # Print the separator
        print('')  # Print another blank line

    # Method to print a single line separator for visual clarity
    def addSingleLineSeparator():
        print('')  # Print a blank line

# Add a triple line separator at the beginning of the output
Toolbox.addTripleLineSeparator()

# Print the title of the code challenge
Toolbox.addTripleLineSeparator()
print('*** Code Challenge - Drawing Shapes ***')
Toolbox.addTripleLineSeparator()

# Base class for shapes
class Shape:
    width = 5  # Default width of the shape
    height = 5  # Default height of the shape
    printChar = '#'  # Character used to represent the shape

    # Method to print the entire shape by iterating through its height
    def print(self):
        for i in range(self.height):  # Repeat the print instruction by the number of rows defined by height
            self.printRow(i)  # Call method printRow with a parameter i that is the row number based on height

# Class representing a square shape
class Square(Shape):
    # Override the printRow method to print a row of the square
    def printRow(self, i): 
        print(self.printChar * self.width)  # Print the printChar '#' for each row as many times as the width (5)

# Class representing a triangle shape
class Triangle(Shape):
    # Override the printRow method to print a row of the triangle
    def printRow(self, i):
        print(self.printChar * (i + 1))  # Print the printChar '#' incrementally based on the row index

# Class representing a more complex triangle shape
class Triangle2(Shape):
    height = 5  # Define a parameter height
    width = 2 * height  # Define a parameter width based on height

    # Override the printRow method to print a row of the triangle
    def printRow(self, i):
        triangleWidth = i * 2 + 1  # Calculate the width of the triangle at the current row
        padding = int((self.width - triangleWidth) / 2)  # Calculate padding to center the triangle
        print(' ' * padding + self.printChar * triangleWidth)  # Print spaces for padding, followed by the triangle width

# Uncomment the following lines to create a Square instance and print it
# s = Square()
# s.print()

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

# Create a Triangle instance and print it
t = Triangle()
t.print()

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

# Create a Triangle2 instance and print it
t = Triangle2()
t.print()
