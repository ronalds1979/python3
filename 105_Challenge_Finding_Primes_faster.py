# Python code​​​​​​‌‌​​‌​‌‌‌‌​‌‌‌​‌‌‌‌​‌‌‌​​ below
# Use print("messages...") to debug your solution.
class Answer:
    def allPrimesUpTo(num):
        allPrimes=[]
        for number in range(2,num+1): # range between 2 and 100, get number
            for factor in range(2, int(number**0.5) +1): # calculate the factor of number and iterate through it number**0.5 is the same of square root of the number
                if number % factor == 0: # test each number, divide number by factor, if the number divided the factor (square root of the number) with remain 0 it is not prime
                    break
            else:
                allPrimes.append(number)
                #print(f'Having {num} as reference {number} is prime!')
        return allPrimes

num = 100
result = Answer.allPrimesUpTo(num)
print (result)