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
print('### Multiprocessing ###')

Toolbox.addTripleLineSeparator()

# there are bugs with the official module
from multiprocessing import Process
#from multiprocess import Process


#LongSquare function to store results in a dictionary
def longSquare(num, results):
    time.sleep(1)  
    print(num**2)  # Store the square of the number in results
    print('Finished computing! ')

start = time.time()  # Record the start time

results = {}  # Initialize an empty dictionary to store results
p1 = Process(target=longSquare, args=(1,results))
p2 = Process(target=longSquare, args=(2,results))

p1.start()
p2.start()

p1.join()
p2.join()

print(results)  # Print the results dictionary

end1 = time.time() - start  # Calculate the elapsed time

print(f'the function took {end1} seconds!')  # Print the elapsed time

# Add a single line separator for visual clarity
Toolbox.addSingleLineSeparator()

#Reference from https://www.digitalocean.com/community/tutorials/python-multiprocessing-example

print('Reference from https://www.digitalocean.com/community/tutorials/python-multiprocessing-example')

import multiprocessing

#To make a parallel program useful, you have to know how many cores are there in you pc. Python Multiprocessing module enables you to know that. The following simple code will print the number of cores in your pc.
print("Number of cpu : ", multiprocessing.cpu_count())

from multiprocessing import Process


def print_func(continent='Asia'):
    print('The name of continent is : ', continent)

def longSquare(num, results):
#    time.sleep(1)  
    print(num**2)  # Store the square of the number in results

if __name__ == "__main__":  # confirms that the code is under main function
    names = ['America', 'Europe', 'Africa']
    procs = []
    proc = Process(target=print_func)  # instantiating without any argument
    procs.append(proc)
    proc.start()

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()


from multiprocessing import Queue

colors = ['red', 'green', 'blue', 'black']
cnt = 1
# instantiating a queue object
queue = Queue()
print('pushing items to queue:')
for color in colors:
    print('item no: ', cnt, ' ', color)
    queue.put(color)
    cnt += 1

print('\npopping items from queue:')
cnt = 0
while not queue.empty():
    print('item no: ', cnt, ' ', queue.get())
    cnt += 1



    from multiprocessing import Lock, Process, Queue, current_process
import time
import queue # imported for using queue.Empty exception


def do_job(tasks_to_accomplish, tasks_that_are_done):
    while True:
        try:
            '''
                try to get task from the queue. get_nowait() function will 
                raise queue.Empty exception if the queue is empty. 
                queue(False) function would do the same task also.
            '''
            task = tasks_to_accomplish.get_nowait()
        except queue.Empty:

            break
        else:
            '''
                if no exception has been raised, add the task completion 
                message to task_that_are_done queue
            '''
            print(task)
            tasks_that_are_done.put(task + ' is done by ' + current_process().name)
            time.sleep(.5)
    return True


def main():
    number_of_task = 10
    number_of_processes = 4
    tasks_to_accomplish = Queue()
    tasks_that_are_done = Queue()
    processes = []

    for i in range(number_of_task):
        tasks_to_accomplish.put("Task no " + str(i))

    # creating processes
    for w in range(number_of_processes):
        p = Process(target=do_job, args=(tasks_to_accomplish, tasks_that_are_done))
        processes.append(p)
        p.start()

    # completing process
    for p in processes:
        p.join()

    # print the output
    while not tasks_that_are_done.empty():
        print(tasks_that_are_done.get())

    return True


if __name__ == '__main__':
    main()
