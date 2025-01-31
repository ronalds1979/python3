#functions to add space lines and traces

def space_lines ():
    return print('')

def space_traces ():
    print('-------')

# Bytes
print (
'''
Bytes

Byte Object Common Uses
Streaming files
Transmitting text without knowing the encondig
Often used "under the hood" in Python libraries
'''
)
print('this creates a empty bytes object that is four bytes long bytes(4)')
print (bytes(4))
space_lines
print("each byte is represented by 'slash x' followed by two hexadecimal or base 16 numbers")
print('Two decimals is 256 possibilities the same as 2 ** 8 ')
print ('the same as 256 possibilities = 2 ** 8 = 8 bits = 1 byte')
space_lines
print('this is four bytes long')
print (bytes(4))
space_lines
sunglasses = bytes('😎', 'utf-8')
print(sunglasses)
print('to allow change it requires to be  byte array')
sunglasses = bytearray('😎', 'utf-8')
print(sunglasses)
print(sunglasses.decode('utf-8'))
space_lines
print ('Update position 3. The last position 0 1 2 3')
sunglasses[3]=int('85', 16)
print(sunglasses)
print ('print the new emoji')
print (sunglasses.decode('utf-8'))
