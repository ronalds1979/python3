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
print('### Multithreading ###')

Toolbox.addTripleLineSeparator()

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

import threading  # Import the threading module for multithreading
import time  # Import the time module again (this is redundant)

# Function to compute the square of a number after a delay
def longSquare(num):
    time.sleep(1)  # Simulate a long computation by sleeping for 1 second
    return num**2  # Return the square of the number

start = time.time()  # Record the start time

# Execute longSquare for numbers 0 to 14 and print the results
print([longSquare(n) for n in range(0, 15)])

end = time.time() - start  # Calculate the elapsed time

print(f'the function took {end} seconds!')  # Print the elapsed time

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

# Redefining the longSquare function to store results in a dictionary
def longSquare(num, results):
    # time.sleep(1)  # Uncomment to simulate a long computation
    results[num] = num**2  # Store the square of the number in results

start = time.time()  # Record the start time

results = {}  # Initialize an empty dictionary to store results

# Create and start threads for numbers 0 to 14
threads = []  # List to hold thread references
for i in range(15):
    thread = threading.Thread(target=longSquare, args=(i, results))  # Create a thread
    threads.append(thread)  # Add the thread to the list
    thread.start()  # Start the thread

# Wait for all threads to complete
for thread in threads:
    thread.join()  # Join each thread, waiting for it to finish

print(results)  # Print the results dictionary

end1 = time.time() - start  # Calculate the elapsed time

print(f'the function took {end1} seconds!')  # Print the elapsed time

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

# Print a new section title for the next part of the code
print('### Multithreading using For loop based in a range ###')

Toolbox.addTripleLineSeparator()

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

# Redefining the longSquare function again (redundant)
def longSquare(num, results):
    # time.sleep(1)  # Uncomment to simulate a long computation
    results[num] = num ** 2  # Store the square of the number in results

start = time.time()  # Record the start time

results = {}  # Initialize an empty dictionary to store results
threads = []  # List to hold thread references

# Create and start threads using a for loop
for n in range(0, 15):
    thread = threading.Thread(target=longSquare, args=(n, results))  # Create a thread
    threads.append(thread)  # Add the thread to the list
    thread.start()  # Start the thread

# Wait for all threads to complete
for thread in threads:
    thread.join()  # Join each thread, waiting for it to finish

print(results)  # Print the results dictionary

end2 = time.time() - start  # Calculate the elapsed time

# Print the elapsed time and compare it to the previous execution
print(f'The function took {round(end2, 4)} seconds! that is {round((end1 - end2), 4)} compared to previous, in percentage is {round(((end1 - end2) / end2) * 100, 2)}% faster')

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()