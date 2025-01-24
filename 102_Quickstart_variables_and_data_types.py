print ('Variables')
print ('### Variables should use lower case ###')
print ('### Variables should not start with number or uppercase ###')
print ('### Variables should not have special characters, except for underline _ ###')

#Defining a variable
x = 5
y = 5.99
a = 'string'
b = True
c = 2j

#Concatenate string
print ('-------')
print ('Concatenate string')
print ("'Good '+'Morning'")
print ('Good '+'Morning')
print ("'1'+'1'")
print ('1'+'1')

#print a variable
print ('Print variables')
print ('x=5 then print (x)')
print (x)

#Data types
print ('-------')
print ('Data Types')

#Number
print ('-------')
print ('Data Type number integer')
print (str('5 is data type ')+str(type (5)))
print ('Variable x contains '+str(str(x)+' that is data type ')+str(type (x)))

#Float
print ('-------')
print ('Data Type number float')
print (str('9.111111 is data type ')+str(type (9.111111)))
print (str('111111.9 is data type ')+str(type (111111.9)))
print ('Variable y contains '+str(str(y)+' that is data type ')+str(type (y)))

#Boolean
print ('-------')
print ('Data Type Logic Boolean')
print (str('True is data type ')+str(type (True)))
print (str('False is data type ')+str(type (False)))
print ('Variable b contains '+ str(str(b)+' that is data type ')+str(type (b)))
print ('print (True)')
print (True)
print ('print (False)')
print (False)
print ('print (1==1)')
print (1==1)
print ('print (1==2)')
print (1==2)
print ('print (True=True)')
print (True==True)
print ('print (True=False)')
print (True==False)
print ('print (2>1)')
print (2>1)
print ('print (1>2)')
print (1>2)
print ('print (1>1)')
print (1>1)
print ('print (1>=1)')
print (1>=1)

#String
print ('-------')
print ('Data Type string')
print (str('Good is data type ')+str(type ('Good')))
print ('Variable a contains '+str(str(a)+' that is data type ')+str(type (a)))
print (str('Good Morning is data type ')+str(type ('Good Morning')))

#String
print ('-------')
print ('Data Type Complex numbers')
print (str('2j is data type ')+str(type (2j)))
print ('Variable c contains '+str(str(c)+' that is data type ')+str(type (c)))

#Convert data type
print ('-------')
print ('Convert data type to string')
print ('Int to string')
print (str (x))
print ('float to string')
print (str (y))
print ('boolean to string')
print (str (b))
print ('-------')
print ('Convert data type to int')
print ('float to int') ## round down the float eg. float 5.99 became 5 int
print (int (y))
print ('boolean to int') ## boolean True = 1 and False = 0
print (int (b))
print ('### IMPORTANT ###')
print ('### we cannot convert string to int data type ###')
## print (int (a))
print ('### IMPORTANT ###')
print ('-------')
print ('Convert data type to float')
print ('int to float') 
print (float (x))
print ('boolean to float') ## boolean True = 1.0 and False = 0.0
print (float (b))
print ('### IMPORTANT ###')
print ('### we cannot convert string to float data type ###')
