#****************************************
#*********DEfining a function************
#****************************************


#Funtion to add 2 numbers
def display_sum(num1,num2):
    print(num1+num2)

# A function will have 
# #1) Function name#
#  2) Inputs 
# #3)Body of the function(what the function actually does)
# 4)output.


#another way to do it.

# def display_sum(num1,num2):
#     sum = num1+num2
#     print(sum)

# #more artistic way to do it.

# def display_sum(num1,num2):
#     sum = num1+num2
#     print("the sum of ",num1,'and',num2,"is",sum)

#How to use defined function?
#ans : we call it

#what u mean by call it?
#ans : It means , at first by defining a function we are creating a new function that is compatable with us....in order to use it again we cannot type the entire code it will be time consuming so thats why we call it by just typing the key word like (display_sum())

# while we define input variables in the function definition , we are creating new 
#variable with scope within the function.

# Well how do i make u understant this , actually when defining a function any thing given with the definition cannot be retained or called outside thats itentation.
#call the function / invoking the number
# display_sum(8,6)                           #the sum of  8 and 6 is 14
# display_sum(2026,8)
# display_sum(9.8,9.6)
# display_sum('happy ','diwali')


# def display_sum_custom():
#     print("we will display the sum of 2 numbers you enter")
#     num1 = float(input("enter the number"))
#     num2 = float(input("Enter the number"))
#     sum = num1+num2
#     print("the sum of ",num1,'and',num2,"is",sum)
    
# #display_sum_custom()   # sum = num1+num2
#                        #print("the sum of ",num1,'and',num2,"is",sum)

# def artificial_int():
#     user = input("Please enter your name :")
#     print("Hi ",user,'\n',"Good Afternoon",'\n',"How are you")



#artificial_int()


#Generating a multiplecation table

# num =5 
# print('multiplication table if' ,num)
# print("******************************")
# for i in range(1,11):
#     print(i,'*',num,'=',(i*num))


# num = 10
# print('multiplication table if' ,num)
# print("******************************")
# for i in range(1,11):
#     print(i,'*',num,'=',(i*num))



# num =265894 
# print('multiplication table if' ,num)
# print("******************************")
# for i in range(1,11):
#     print(i,'*',num,'=',(i*num))



# num =123654789456123
# print('multiplication table if' ,num)
# print("******************************")
# for i in range(1,11):
#     print(i,'*',num,'=',(i*num))


# Function to display multiplication table of any function.

# def multiplication_table():
#     num = int(input("Please enter the Number you want the Multiplication Table of : "))
#     print("*************************************************************************")
#     print('multiplication table if' ,num)
#     print("******************************")
#     print("Heres your results")
#     for i in range(1,11):
#         print(i,'*',num,'=',(i*num))
#         print(f"{i} x {num} = {i*num}")


#multiplication_table()             #invoking the function


#We need to get scores
#1. sum of scores
#2. Average score
#3. largest
#4. smallest


# def score_input():
#     y= int(input("Please input the First score :"))
#     u= int(input("Please enter the second code :"))
#     i= int(input("please enter the third score :"))
#     o= int(input("Please enter the fourth score :"))
#     p= int(input("Please enter the fifth score :"))
    
#     return [y,u,i,o,p]

# def score_total(score):
#     total = sum(score)
#     print("Total score achieved:", total)



# #def score_average(loop):
#     for i in range(len(loop)):
#         average = score_total(loop)/len(loop)
#         print("The average score of the student is : ",average)


# marks = score_input()
# score_total(marks)
# score_average(marks)
    




# def calculate_sum(score_list):
#     sum = 0
#     for i in range(len(score_list)):
#         sum = sum + score_list[i]
#     print(f'total score = {sum}')
#     return sum



# def calculate_sum_2(score_list):
#     sum = 0
#     for i in range(len(score_list)):
#         sum = sum + score_list[i]
#     print(f'total score = {sum}')
#     return sum



# scores = [20,30,20,30,40]
# # total = calculate_sum(scores)

# def calculate_avg(score_list):
#     total = calculate_sum_2(score_list)
#     count = len(score_list)
#     average = total/count
#     print(f'Average score = {average}')
#     return average


# score1 = int(input(' PLease enter the score 1 - '))
# score2 = int(input(' PLease enter the score 2 - '))
# score3 = int(input(' PLease enter the score 3 - '))
# score4 = int(input(' PLease enter the score 4 - '))
# score5 = int(input(' PLease enter the score 5 - '))

# scores = (score1, score2, score3, score4, score5)
# print(scores)


# def calculate_sum(input_tuple):
#     sum = 0
#     for i in range(len(input_tuple)):
#         sum = sum + input_tuple[i]
#     print(f'The sum of scores = {sum}')
#     return sum                                      # output of the function

# # total = calculate_sum(scores)                          # whenever their is an output we assign it to a variable


# def calculate_average(input_tuple):
#     total = calculate_sum(scores)
#     count = len(input_tuple) 
#     average = total / count
#     print(f'Average of  Scores = ', average)
#     return average


# # calculate_average(scores)

# def find_large():
#     large = max(scores)
#     print(f'The largest score is - ', large)

# # find_large()

# def find_small():
#     small = min(scores)
#     print(f"The lowest score is - ", small)

# # find_small()


#**************************************************
#*****************optional argument*****************
#***************************************************



# def calculate_exponent(num,exp=2):  #here , exp is an opyional input,default value is 2
#     print(num**exp)


# calculate_exponent(5,3)
# calculate_exponent(5)



# def create_wish(name,wish= 'Good day'): # while in this case the exceptional value value is wish.what happens here is even if we dont give anything as input the already given default value will display.
#     print(f'hi {name},{wish}')

# create_wish("Gowtham")
# create_wish("Gowtham","Happy diwali")        #here positional argument is used

# create_wish(wish= "happy diwali",name="gowtham")  #We can givev values of arguments explicitly.


#**************************************************************************************
#**************************************************************************************
#**************************************************************************************


def divide(num,den):
    result = num/den
    print(f'The answer is{result}')


divide(9,2)
divide(5623,5)

divide(0,500)
#divide("a","b") # type error #the error that happens while running a program is called Run time error . there are many types of run time error.
# exception handling.
# we write specific critiria so that code flow is not interrupted.
#we write potential runtime errors making code inside 'try' block.
# and the exep




def divide_new(num,den):
    try:                             # by using this method we can by pass if an error occurs and move forward to the next code line without stopping the whole program.
        result = num/den
        print(f'The answer is{result}')
    except:
        print(f"There is a problem")
        print("some error has occured")
    print("*********************************************************")
    print("You have rechead the end of the program")

divide_new(9,2)
divide_new(5623,5)
divide_new(5623,0)
divide_new("a","b")



#rewriting the function with exception block displaying the error message.

def divide_new1(num,den):
    try:                             # by using this method we can by pass if an error occurs and move forward to the next code line without stopping the whole program.
        result = num/den
        print(f'The answer is{result}')
    except Exception as e:            # while using this it actually prints whats the specific problem happened in the program.
        print(f"There is a problem : {e}")
      
    
divide_new1(9,2)
divide_new1(5623,5)
divide_new1(5623,0)
divide_new1("a","b")


def divide_new2(num,den):
    try:                             # by using this method we can by pass if an error occurs and move forward to the next code line without stopping the whole program.
        result = num/den
        print(f'The answer is{result}')
    except TypeError:            # while using this it actually prints whats the specific problem happened in the program.
        print(f"Please make sure you are entering numbers")
    except ZeroDivisionError:        # if this zerodivision error is seen it is detected.
        print("Please make sure to give a non zero value as denominator ")
    except Exception as e:
        print(f'There is problem :{e}')
    print("end")


        
divide_new2(9,2)
divide_new2(5623,5)
divide_new2(5623,0)
divide_new2("a","b")



