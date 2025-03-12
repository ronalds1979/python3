
def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)
    
    # 5 + 4 = 9
    # 5 + 3 = 8
    # 5 + 2 = 7



def square(num):
    return triangle(num) + triangle(num-1)

print(square(5))
print(square(6))

# From Chapter quiz

def someFunc(func):
    print(func(5) + 2) # (3 * 5) + 2

someFunc(lambda x: x * 3) # 3 * 5
