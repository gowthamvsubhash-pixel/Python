# #set and dictionary uses this'  {}  '  this bracket.

# #declaring a set

# set1 = {}   #this is not a set, this is a dictionary

# #method 2

# set2 = {12,55,88, 2020, True, 'Bsnl', 2020, 2020.0,'2020'}


# #method 3

# set3 = set()


# print(type(set1))
# print(type(set2))
# print(type(set3))


# print(set2)     # values were displayed but not in the order.


# # set supperts all datatypes. i.e ; Hetrogrnous
# # set will not allow same values to repeat.(duplicates are not allowed)
# # duplicates are not allowed , they are deleted.


# # a collection of values which cannot repeat.
# # ven diagram - 
# #intersection - the common values in two sets.
# # union - combining two sets.
# # difference - 

# print('************************Functions*******************************')


# roll = {1,2,3,4,5,6}
# roll_odd = {1,3,5}
# roll_even = {2,4,6}
# random = {1,5,9,4}

# random.add(2026) # add method is used to add values to the set.
# print(random)    #{1, 4, 5, 9, 2026}

# random.copy()
# print(random)

# #difference between sets(present in random but not in roll_odd)
# print(random.difference(roll_odd)) #{{9, 2026, 4}}
# print(roll_odd.difference(random)) #{3}


# print(roll.issuperset(roll_odd)) #True
# print(roll.issuperset(random)) # False
# print(roll.issuperset(roll_even)) #True
# print(roll.issubset(random)) #False
# print(roll_odd.issubset(roll)) #True


# print(roll.intersection(random)) #{1, 4, 5}
# print(roll.isdisjoint(random))

# roll.discard(4)
# print(roll)

# #***************properties of set******************************

# # supports hetrogenius data types
# #cannot acces data using index
# # duplication is not allowed
# #mutable

# #*******************************************************************************
# #*********************************** Dictionary ********************************
# #*******************************************************************************


# # key - the value that we refer.Every key is unique ,it will not repeat.


# declaring a dictionary

dict1 = {}   #this is not a set, this is a dictionary

#method 2

# Dict2 = {'key1' : 'value1', 'key2' : 'value2',8 : 2029, True : 'Yes it works'} #this is a dictionary


# #method 3

# Dict3 = dict()



# print(type(dict1))
# print(type(Dict2))
# print(type(Dict3))

# print(Dict2)

# # a dictionaries keys can be of any datatype.


# sample_dictionary= {1: 'one',2: 'two', 0: 'zero', 1: 'ict'} # if we give duplicate value , it will check and assign the latest one.

# # print(sample_dictionary) #{1: 'ict', 2: 'two', 0: 'zero'}# because ict was the last input ,therefore it becomes the latest value to key 1.

# # print(Dict2['key2'])    #dictionary[key] = value associated with the key, in this case it is printed as "value2".





# student_dict = {'name ': 'Gowtham',
#                 'age' : 22,
#                 'university' :'MG',
#                 'district' : 'kottayam'}

# # pirnting the whole dictionary
# print('Whole dictionary')
# print(student_dict)
#              #Whole dictionary
# #              {'name ': 'Gowtham', 'age': 22, 'university': 'MG', 'district': 'kottayam'}


# #print values alone
# print('Values are ')
# print(student_dict.values())
#           #Values are 
#            #dict_values(['Gowtham', 22, 'MG', 'kottayam'])


# print(student_dict.items())
#              #dict_items([('name ', 'Gowtham'), ('age', 22), ('university', 'MG'), ('district', 'kottayam')])


# student_dict['university'] = 'Kerala university'  # this funtion will work so it is a mutable datatype.
# print(student_dict) #{'name ': 'Gowtham', 'age': 22, 'university': 'Kerala university', 'district': 'kottayam'}



personal_info = {'name': 'Gowtham V Subhash',
                 'E-Mail':'gowthamvsubhash@gmail.com',
                 'Mobile number': '623839685',
                 'Home town': 'Mundakyam',
                 'Currently': 'Student'}


print('Personal info')
print('***************************************************')

print(personal_info)


input_value2 = input('Please enter which info u want to change'.capitalize())
input_value = input("Please enter the info u want to change")
if(input_value2 == personal_info):
   print('This are the info')
else:
    print('Invalid Information ')    

personal_info['name'] = input_value
print(personal_info)
                                                    #{'name': 'aswanth', 'E-Mail': 'gowthamvsubhash@gmail.com', 'Mobile number': '623839685', 'Home town': 'Mundakyam', 'Currently': 'Student'}
print('******************************************************')

