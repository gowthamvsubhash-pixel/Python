# fruits = ["apple", "banana", "orange", "mango"]
# no_of_fruits = 6

# i = input('Plese enter the fruit u want to add')
# n = int(input('plese enter the place where u want it to be'))
# if(n>no_of_fruits ):
#     print(" the number u have entered is out of self items")
#     print(" These are the available shelf numbers",'1 ->',no_of_fruits)
# else:
#     fruits.insert(n,i)
#     fruits.append("odhalanga")
#     print(' These are the fruits which are available : ',fruits)

# print('****************************************************************************')



# def count_even():
#     count = 0

#     for i in range(5):
#         n = int(input("Please enter a number: "))

#         if n % 2 == 0:
#             print(n, "is even")
#             count += 1

#     print("Total even numbers:", count)



def count_even(numbers):
    count = 0

    for i in numbers:
        if i % 2 == 0:
            count += 1

    return count


numbers = [10, 15, 20, 25, 30, 35]

result = count_even(numbers)

print("Total even numbers:", result)