def loop_fact(a,result):
    while a >= 1:
        result = result * a
        a = a - 1
    return result

def factorial(num):
    a = num-2
    result = num * (num-1)
    return loop_fact(a,result)

class Process:
    # __init__ function is a special one, stand for initialization. It is called whenever an instance of the class is created
    # the variable self is the specific instance of the class after we have initialized it
    # self represent the instances of the class. These classes instances are the objects.
    # the variable (num) inside the class are the attributes of the objects
    # the function (factorial) inside the class are the methods. The dog object has the method speak
    def __init__(self):
        self.nothing = 1
    def factorial(self,num):
        if type(num) != int:
            return None
        if num < 0:
            return None
        if num == 0:
            return 1
        if num > 0:
            return factorial(num)
        else:
            return None

# use the class
#set a variable to call the class Process
Answer = Process()
#set the variable number
number = 52
#use the variable Answer to call the Class using the method factorial providing the variable number as parameter add the result to the variable result and print it
result = Answer.factorial(number)
print (result)

#factorial('spam spam spam spam spam spam')
#factorial(1.2)
#factorial(-2)
#factorial(0)
#factorial(5)