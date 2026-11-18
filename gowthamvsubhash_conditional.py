
#1
number = input('Please enter a number')
number = int(number)

if(number >= 1):
    print('The number u have entered is a positive number')
else:
    if(number <= 1):
        print('The number u have entered is a Negative number')


#2
Age = input('Please enter your age for further processing')
Age = int(Age)

if(Age >= 18):
    print('The person is eligible to vote')
else:
    print('The person is underage,Not eligible to vote')


#3

number = input('Please input a integer number')
number = int(number)

if(number %2==0):
    print('the number u have entered is even')
else:
    print('The number u have entered is odd')

#4

Password = input('please enter your password')
password ="2222"

if(password ==2222):
    print('Access Granted')
elif(password != 2222):
     print('Access Denied')


#5
numb_1 = int(input('Please enter first number'))
numb_2 = int(input('please enter second number'))

if(numb_1>numb_2):
    print('numb_1 is greater',numb_1)
elif(numb_1 < numb_2):
    print('num_2 is greater',numb_2)
else:
    if(numb_1 == numb_2):
        print('both are equal') 


# 6

marks = float(input('Enter your marks out of 100'))

if(marks>100):
    print('the mark u entered is invalid')
elif(marks>=90):
    print('you received A grade')
elif(marks>=80):
    print('you recieved B grade')
elif(marks>=70):
    print('you have receievd a C grade')
elif(marks>=60):
    print('you received a D grade')
elif(marks>=50):
    print('you received a E grade')
elif(marks<50):
    print('you failed the exam,enitt podey')
elif(marks<0):
    print('invalid marks')


# 7

no_1 = int(input('please enter the first number'))
no_2 = int(input('please enter the second number'))
no_3 = int(input('please enter the second number'))

if((no_1 > no_2) and (no_1 > no_3)):
       print('this number is the biggest one',no_1)
elif((no_2 > no_1) and (no_2 > no_3)):
   print('This is the biggest number',no_2)
elif((no_3 > no_2) and (no_3 > no_1)):
   print('this is the biggest number',no_3)


# 8 

traffic = input('Enter a traffic light colour')

if(traffic == 'Red'):
    print('stop')
elif(traffic == 'Yellow'):
    print('Get ready')
elif(traffic == 'Green'):
    print('GO')
else:
    print('invalid output')

#9

unit = float(input("enter how much electricity you enjoyed"))

if(unit <= 100):
    print('Total bill amount', unit*2)
elif(unit <= 200):
    print('Total bill amount',200+(unit-100)*3)
elif(unit <= 300):
    print('Totl bill amount',500+(unit-200)*5)
elif(unit >300):
    print('Total bill amount',1000+(unit-300)*7)

#10

account_balance = float(10000)

amount = int(input('Enter the withdrawl amount'))

if(amount < 0):
    print('The amount is not withdrwable')
elif(amount < 0):
    print('the amount is not positive')
elif(amount%100!=0):
    print('The amount is not a multiple of 100')
elif(amount>account_balance):
    print('insufficient balance')
else:
    print('your account balance is',account_balance-amount )
