# # #  list -  is a datatype used to store a collection of values

# # # since its a combination of other data types (int, float,string,boolean) , we call it as a derived datatype.

# # #There is no restriction in terms of datatypes  in a list.
# # # A list can contain varies types of data. therefore it is called as hetrogenius data.

# # # declaring a list

# # lst_names = []
# # print(type(lst_names))

# # name =""
# # print(type(name))

# # # declaring a list

# # #Method 1

# # lst_names1 = []
# # print(type(lst_names1))

# # #method 2

# # lst_names2 = ['gowtham','Akash','arjun']
# # print(type(lst_names2))

# # #method 3

# # lst_names3 = list()
# # print(type(lst_names3))

# # # fetching values using index from a list.

# # print(lst_names2[0])
# # print(lst_names2[1])
# # print(lst_names2[2])

# # #print(lst_names2[3]) #there is not any 4 th value in that list so it creates a syntex error.

# # # list containg multiple data types.

# # # personal - information as a list
# # # personal info as a list : name , age , graduation year , university , height, frinds

# # amar_info = ["amar",22,2026 , 'CUSAT',175.5 , lst_names2]
# # print(type(amar_info))


# # print(amar_info[0])             # display value at index = 0
# # print(type(amar_info[0]))        # display data tyoe of value at index = 0

# # print(amar_info[1])             # display value at index = 1
# # print(type(amar_info[1]))       #display data type of value at inddex = 1

# # print(amar_info[2])             #display value at index = 2
# # print(type(amar_info[2]))       #display data type of  value at index = 2
 
# # print(amar_info[3])             # display value at index = 3
# # print(type(amar_info[3]))       #display data type od value at index = 3

# # print(amar_info[4])             #display value at index = 4
# # print(type(amar_info[4]))        # display data type of value at index = 4

# # print(amar_info[5])            # display value at index = 5
# # print(type(amar_info[5]))       # display data type of value at index = 5

# # contagination - combining of two strings





# # list = [1,2,3]

# # list2 = [False,True, False]

# # print(list + list2)   # list contagination




# #*******************************************************
# #***************List Functions**************************
# #*******************************************************



# list = [1,7,3]

# list2 = [False,True, False]
# lst_name = ['Gowtham', 'Akash', 'Arjun']

# print(list)
# list.sort()
# print(list)

# print(lst_name)       #unsorted
# lst_name.sort()       #Giving command to sort
# print(lst_name)       #printing the sorted data {1,3,7}


# list.sort(reverse= True)  #sort the other way from the back to the begining
# print(list)   # PRinting reversed output [7,3,1]

# lst_name.sort(reverse=True)
# print(lst_name)


# # lst_name2 = ['Gowtham','Akash','Arjun',7,3,1]

# # lst_name.extend(list)
# # print(lst_name)

# # list2.extend(list)
# # print(list2)

# # list2.append(list)   # list 1 was added as the last value of list2
# # print(list2)

# # print(list2)
# # print(list2[3])

# # list.append('A')
# # print(list)


# #*******************************************************************

# home = ['soft','hard','mild']

# work = ['excel', 'point' , 'crown']

# print(home[0])

# home.append(work)
# print(home)

# print(work[2])


# #*****************************************************************


# # reverseing a list

# list.reverse()   # ['A', "1","2","3"]
# print(list)


# list2.count(False)         # check the count of value ' False '
# print(list2)


# print('the no of times false appear in the list = ', list2.count(False))
# print('the number of times true appears in the list =', list2.count(True))
# print("the number of times 'X' appear in the list = ", list2.count('X'))


# # value at the last index

# print(list2[-1])

# # Fetch number of items in the list

# len(list2)
# print('total number of elements in', list2,'is',len(list2))


# #value at the last index

# print(list2[-1])
# print(list2[len(list2)-1])


# print('********************************************************************************************')

# print('before clear')
# print(list2)

# list2.clear() #clear all value from variable.

# print('after clear')
# print(list2)     # after commanding clear it will just disapprer, it will be erased (all the values in that variable)


# print('***************************************************************************************************')

# print('before inserting any value',list) #[7,3,1,'A']
# #in order to do #[7,3,1,'A']  ->  [7,3,100,1,'A']

# list.insert(3,100)    # This is how inserting 100 at index    #before inserting any value [1, 3, 7] After inserting any value [1, 3, 7, 100]
# print('After inserting any value',list)

# print('*****************************************************************************************************')

# print('before removing 3', list) # before removing 3 [1, 3, 7, 100]
# list.remove(3)
# print('after removing 3',list)  #after removing 3 [1, 7, 100]

# print('*****************************************************************************************************')

# list.pop()
# print(list)

# #********************************************************************
# #***********************Tuple****************************************
# #**********************************************************************



# # Tuple  -> also contains hetrogenius data 
# # the simple difference between tuple and list is the brackets, list is in [] ,while tuple is using ().
# # there is no restictions in terms of datatypes in a tuple.

# #declaring a tuple
# tuple1 = ()
# tuple2 = (2026, 'Nov',3.75,False,[8,True,9.8])
# tuple3 = tuple()

# print(type(tuple1)) #<class 'tuple'>
# print(type(tuple2)) #<class 'tuple'>
# print(type(tuple3)) #<class 'tuple'>


# print(tuple2[2])

# tuple1.count(False)
# print(tuple2.count(False))
# print(tuple2.index('Nov'))


# # once the tuple is created we cannod make changesnto it 


# # list -> mutable (can make changes to value)
# # tuple -> immutable  ( cannot make changes to values)


# del(tuple2)   # we are deleting that tuple
# del(list2)    # we are deleting that list


# print(tuple2)         # it will run as a error because there is not a varient in that name exist anymore 