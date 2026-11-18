#************************************************************
#**********checking whether a number uis bigger than 50****************
#**************************************************************

# number = input('Please enter a number :')    #get user innput
# number_int = int(number)                       # converts the input as a nnumber
# if(number_int > 50):           # we can only further process only if the colon':'is given
#      print('The number you enterd is bigger than 50')

# if(number_int < 50):
#     print('The number you entered is lower than 50')
    
# print('End of the program')


#number>50 # 'The number entered is bigger than 50
#umber<50 # 'the number enteredis bigger than 

# Intentation -
#when giving control statements , we give coloums

# we can use python tutor website to practice to study

#inentation
# if(number_int > 50):
#     print('The number entered is bigger than 50')
# else:
#     print('The number entered is not bigger than 50')

# print('End of program')

# number = input('enter a number that we need to check as even or odd')
# number_int = int(number)

# if(number_int % 2==0):
#     print('The entered number is an even number')
# else:
#     print('The entered number is an odd number')

# = is as assigning operater while if u want calculation give '=='

#*********************************************************************
#********************************************************************

# temp = input('please enter the Temperature in celcius')
# temp = float(temp)
# >= 35 : Very hot
# 25 - 35 : Warm
# 15 - 25 :cold
# #<= :freezing

# if(temp >=35):
#     print(' its a very hot day')
# else:
#     if(temp >= 25):
#         print(' Its a warm day')
#     else:
#         if(temp >=15):
#             print('its a cold day')
#         else:
#             if(temp <=15):
#                 print('freezing cold')


# Nested if else loop

# if(temp >=35):
#     print('Its a very hot day')
# elif(temp >=25):
#     print('Its a warm day')
# elif(temp >=15):
#     print('Its a cold day')
# else:
#     print('Freezing day')

#**************************************************8
#****************iterative statements***************************
#*****************************************************8

# iterative statements are used when certain tasks are to be executed multiple times

# loop - its circle around and end at the begining it self
#forloop - when no of iteration is knowwn

#while-loop - No.of iteration are unknown,But stopping condition is known.
      # if ending condition is not given it would run again and again without stopping.We should bre careful when using iterative while loop.
      #only givee while-loop if end condition is known

# pritn your name 10 times

# for i in range(10):        # we are giving number of iterations
#     print(i,': Gowtham')       #iterative( repatative) tasks


# print('using step operator')

# for i in range(10,2):        # we are giving number of iterations
#     print(i,': Gowtham')       # syntax error means grammer mistake in language

#python will only execute if the begining starting point is greater than ending point.
# # range( start, end , step)
# if range is not mentioned ,it takes step value as '1'.

# for i in range(3,10,3):
#     print(i , ': Gowtham')

# for i in range(10,3,-3):
#     print(i , 'Gowtham')

#     #ending point is not included like if ending point is given as 10 and step as 1 it would count only till 9, it happens because the commond says until 10,which does not include 10.

# print('Odd numbers')

# for i in range(1,50,2):
#     print(i , ':Odd number')

# print('Odd numbers from 20 to 50')

# for i in range(21,50):
#     if(i % 2 !=2):
#         print(i , '-:ODD numbers between 20 and 50')

#************************************
# **********while- loop************** 
#************************************


# num = 1
# while(num < 10):
#     print(num)
#     num = num + 1

# print('end of while loop')

# Always remember to give end condition

# num = 1
# while(num < 50):
#     print(num)
#     num = num + 2

# print('\n','odd numbers between 20 and 50')
# num = 21
# while(num < 50):
#     print(num , end =',')
#     num = num + 2

# ippam ee number output ayi varunnath 1,2,3,4,.... inkane varanam enkil orr end satatement mandel kodutha pole koduthal mathi athil quate cheyth orr couma kudi kodukkuka.

age = int(input('Enter your age'))


valid_id = input('do you have a valid id card (y/n):')


if (valid_id =='y'):
    valid_id = True
else:
    valid_id = False


print("We are checking your details")

if(age >= 18):
    if(valid_id):
        print("you are eligible to vote")
    else:
        print("you are not eligible to vote")
        print('you need a valid id card to vote')
else:
    print('you are not eligible to vote')
    print('you should be 18 or older to be eligible')

print('...................................................')


#doing the same process using logical expression

if(age >= 18) and (valid_id):
    print('you are eligible to vote')
else:
    print('you are not eligible to vote')
     

