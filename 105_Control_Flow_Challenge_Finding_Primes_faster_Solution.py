def AllPrimesUpTo(num):
    primes=[2] # start the primes list with 2
    for number in range(3, num): # go through the range 3-num to check if there is any prime number
        sqrNum = number**0.5 # calculate the square root of number
        for factor in primes:
            if number % factor == 0:
                break # not prime
            if factor > sqrNum:
                primes.append(number) # it is prime
                break # it is prime
    return primes

num = 100
result = AllPrimesUpTo(num)
print (result)

print(['Monty Python' if n % 6 == 0 else 'Python' if n % 3 == 0 else 'Monty' if n % 2 == 0 else n for n in range (1,10)])