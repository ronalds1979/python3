## Data Structures
print ('### Data Structures ###')

print ('### Lists ###')
print ('List is a collection which is ordered and changeable. Allows duplicate members. Lists include list of any data type and list of lists. It use square brackets. Order is important for list')
print ('-------')

my_list = [1,2,3,4]
print ('Print the list')
print (my_list)
print ('Check if an item is on the list')
if 1 in my_list:
    print ('1 is on this',my_list)
print('print 0 the first item in the list')
print (my_list[0])
print('print 1 the second item in the list')
print (my_list[1])
print('print -1 refers to the last item')
print (my_list[-1])
print('print -2 refers to the second last item etc')
print (my_list[-2])
print('print a range 0:3 from first to third item item 3 the fourth is not included')
print (my_list[0:3])
print('print a range :3 from first to third item item 3 the fourth is not included')
print (my_list[:3])
print('print a range 2: from third item 2 to the end')
print (my_list[2:])

print (type (my_list))
print (len (my_list))

my_list_string = ['monday','tuesday','wednesday','thursday']
print (my_list_string)
print (type (my_list_string))
print (len (my_list_string))

my_list_all = ['monday',1,True,1.1]
print (my_list_all)
print (type (my_list_all))
print (len (my_list_all))

my_list_list = [['monday','tuesday'],[1,2,3],[True,False],[1.1,1.2]]
print (my_list_list)
print (type (my_list_list))
print (len (my_list_list))

print ('order is important for list')
print([1,2]==[1,2])
print([1,2]==[2,1])

print('append an item to the end of list')
my_list = [1,2,3,4]
print (my_list)
print (len (my_list))

print ('change a list item')
print ('original list')
my_list = [1,2,3,4]
print (my_list)
print ('change 0 in this case 1 to 7')
my_list[0]=7
print (my_list)

print ('change a range of list item')
print ('original list')
my_list = [1,2,3,4]
print (my_list)
print ('change 0:2 in this case 1,2 to 8,7')
my_list[0:2]=[8,7]
print (my_list)

print ('append 5 to a list')
my_list.append(5) 
print (my_list)
print (len (my_list))
print ('number of occurences of an entry on the list')
print (my_list.count(4))

print ('### Sets ###')
print ('Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members. Sets include any data type. It use curly brackets. Order is not important for sets. Sets have unique values')
print ('-------')
my_set = {1,2,3,4}
print (my_set)
print(type(my_set))
print(len(my_set))

my_set_duplicated = {1,1,2,2}
print('my_set_duplicated = {1,1,2,2}')
print (my_set_duplicated)
print(type(my_set_duplicated))
print(len(my_set_duplicated))
print ('order is not important for set')
print({1,2}=={1,2})
print({1,2}=={2,1})

print ('### Tuples ###')
print ('Tuple is a collection which is ordered and unchangeable. Allows duplicate members. Tuples include list of any data type and list of lists. It use parenthesis. Order is important for tuples. We cannot append new data for tuple, it is memory efficient')
print ('-------')

my_tuple = (1,2,3,4)
print (my_tuple)
print (type (my_tuple))
print (len (my_tuple))

print ('order is important for tuple')
print((1,2)==(1,2))
print((1,2)==(2,1))

print ('### Dictionaries ###')
print ('Dictionary is a collection which is ordered** and changeable. No duplicate members. Dictionaries have unique key and a definition for the unique key')
print ('-------')
my_dictionary = {
    'apple' : 'A red fruit',
    'bear' : 'A scary animal'
}
print (my_dictionary)
print ('The definition of apple an item of my_dictionary')
print (my_dictionary['apple'])

