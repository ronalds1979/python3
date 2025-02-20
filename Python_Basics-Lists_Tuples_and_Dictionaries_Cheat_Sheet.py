#Lists are created with [ ]
L = [1, 2, 3, 4, 5]
print('List L content')
print (L)
print ('')
print ('---------------------------------------------------')
print ('')

#Tuples are created with ( )
T = (10, 20, 30, 40, 50)
print('Tuple T content')
print (T)
print ('')
print ('---------------------------------------------------')
print ('')

#Returns 1st element of L (1)
L[0]

#Returns 1st element of T (10)
T[0]

#Returns 2nd to 4th element of L ([2, 3, 4])
L[1:4]

#Returns 2nd to 4th element of T ((20, 30, 40))
T[1:4]

#Returns 1st to 2nd last element of L skipping one at a time ([1, 3])
L[0:-1:2]

#Returns 1st to 2nd last element of L skipping one at a time ((10, 30))
T[0:-1:2]

#Assigns 22 to 2nd element of L (L == [1, 22, 3, 4, 5])
L[1] = 22

#T[1] = 22
#ERROR: You can't assing anything to tuples

#Assigns 11 and 22 to 1st and 2nd element of L respec­tively (L == [11, 22, 3, 4, 5])
L[0:2] = [11, 22]


#List Methods

#set list a and b
print ('List a and b')
a = ['a', 'b', 'c']
b = [1, 3, 2]

print (a)
print (b)
print ('')
print ('---------------------------------------------------')
print ('')

print ("Returns the index of the first occurrence of 'b' (1)")
a.index('b')
print (a.index('b'))
print ('')
print ('---------------------------------------------------')
print ('')

print("Returns a concatenated with b (['a', 'b', 'c', 1, 3, 2])")
a + b
print (a + b)
print ('')
print ('---------------------------------------------------')
print ('')

print ("Returns True if 'c' is in the list a and False otherwise (True)")
'c' in a
print ('c' in a)
print ('')
print ('---------------------------------------------------')
print ('')


print ("Returns the number of elements in a (3)")
len(a)
print (len(a))
print ('')
print ('---------------------------------------------------')
print ('')

print ("#Appends 'd' to the end of the list a (a == ['a', 'b', 'c', 'd'])")
a.append('d')
print (a)
print ('')
print ('---------------------------------------------------')
print ('')

print ("Appends every element of the iterable to the end of a (a == ['a', 'b', 'c', 'd', 'e', 'f'])")
a.extend(['d', 'e', 'f'])
print (a)
print ('')
print ('---------------------------------------------------')
print ('')

print ("Inserts 'd' to index 1 of a (a == ['a', 'd', 'b', 'c', 'd', 'd', 'e', 'f'])")
a.insert(1, 'd')

print (a)
print ('')
print ('---------------------------------------------------')
print ('')

print ("Returns the last element of the list and deletes it from the list. ('f')")
print (a.pop())
print(a)
print ('')
print ('---------------------------------------------------')
print ('')



print("Returns 2nd element of a and removes it from the list ('b')")
print (a.pop(1))
print(a)
print ('')
print ('---------------------------------------------------')
print ('')

print("Removes first occurrence of 'b' in a (a == ['a', 'c'])")
print (a)
a.remove('b')
print (a)
print ('')
print ('---------------------------------------------------')
print ('')

print("Clears the list entirely (a == [])")
print (a)
a.clear()
print (a)
print ('')
print ('---------------------------------------------------')
print ('')

print("Returns the number of occurr­ences of 'b' in a (1)")
print (a)
print(a.count('b'))
a.append('b')
print (a)
print(a.count('b'))
print ('')
print ('---------------------------------------------------')
print ('')

print("Returns a sorted version of b ([1, 2, 3])")
print (b)
b.sort()
print ('after sort')
print (b)
print ('')
print ('---------------------------------------------------')
print ('')

print ("Reverses the list a (['c', 'b', 'a'])")
a = ['c', 'b', 'a']
print (a)
a.reverse()
print ('after reverse')
print (a)
print ('')
print ('---------------------------------------------------')
print ('')

print ("Returns a copy of a")
print ("The copy() method returns a list identical to the original, but with a different ID. It means that they are allocated in different places of memory")
print ('list a')
print (a)
c = a.copy()
print ('list c, copy of a')
print (c)
print ('')
print ('---------------------------------------------------')
print ('')

print ("Tuple methods")

t1 = ('a', 'b', 'c')
t2 = (1, 2, 3)

print ("Returns a concatenated version of t1 and t2")
print ('tuple t1')
print (t1)
print ('tuple t2')
print (t2)
print ('t1 + t2 concatenated')
print (t1 + t2)
print ('')
print ('---------------------------------------------------')
print ('')

print ("Returns True if 2 is in t2 and False otherwise (True)")
print (t2)
print (2 in t2)
print ('')
print ('---------------------------------------------------')
print ('')

print ("Returns the number of elements in t1 (3)")
print (t1)
print (len(t1))
print ('')
print ('---------------------------------------------------')
print ('')

print("Returns the number of occurrences of 2 in t2 (1)")
print (t2)
print (t2.count(2))
print ('')
print ('---------------------------------------------------')
print ('')

print ("Returns the index of the 1st occurrence of 1 (0)")
print (t2.index(1))
print ('')
print ('---------------------------------------------------')
print ('')

print ("List loops 1")

a = ['one' , 'two', 'three']
print (a)
for i in a:
    print(i)
print ('')
print ('---------------------------------------------------')
print ('')

#List loops 2

a = ['one' , 'two', 'three']
print(a)
for i in range(len(a)):
    print(f"a[{i}] == {a[i]}")
print ('')
print ('---------------------------------------------------')
print ('')