

#1


students_list = ['Gowtham','Akash','Arjun','Dhineshan','CC']

u = input('Plese enter the name of the new admission : ')

students_list.append(u)
print(students_list)

#Updated list of admission : ['Gowtham', 'Akash', 'Arjun', 'Dhineshan', 'CC', 'sakriya']


#2


list1 = ["Rice","Sugar","Milk"]
list2 = ["Bread","Eggs","Butter"]

list1.extend(list2)
print('Your current shopping list is : ', list1)
               #['Rice', 'Sugar', 'Milk', 'Bread', 'Eggs', 'Butter']

len(list1)
print('total number of items to purchase : ',len(list1))
        #total number of items to purchase :  6


#3



numbers = [10, 20, 10, 30, 40, 10, 20, 50]

i = int(input(' Kindly please enter a number : '))
                   #Kindly please enter a number : 10

print('this much time this number exists in our server : ',numbers.count(i))
                 # this much time this number exists in our server :  3  


#4


n = [1,2,3,4,5,6,7,8,9,10]
n.reverse()
print('Reversed numbers : ',n )
          #Reversed numbers :  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


#5


marks = [ 78, 45, 92, 56, 88, 34, 67]

marks.sort()
print('Marks in Ascending order : ',marks)
          #Marks in Ascending order :  [34, 45, 56, 67, 78, 88, 92]


marks.reverse()


print('Marks in Dscending order :', marks)
#                #Marks in Dscending order : [92, 88, 78, 67, 56, 45, 34]



# 6


fruits = ["Apple", "Banana", "Mango", "Orange"]

f = input('Enter a fruit name : ')
g = int(input('which position do u want the fruit to be added : '))

fruits.insert(g,f)


print(fruits)


# Enter a fruit name : pappaya
# which position do u want the fruit to be added : 2
#['Apple', 'Banana', 'pappaya', 'Mango', 'Orange']


# 7 


subjects = ["English", "Maths", "Science", "Computer", "History"]

print(subjects)
print(subjects.pop())


print(subjects)

#['English', 'Maths', 'Science', 'Computer', 'History']
#History
#['English', 'Maths', 'Science', 'Computer']



#8


colours = ["Red", "Blue", "Green", "Yellow", "Blue"]

c = input('Please enter the colour that u want to remove : ')

colours.remove(c)

print(colours)

         # Please enter the colour that u want to remove : Red
           #['Blue', 'Green', 'Yellow', 'Blue']


# 9

l = ["Python","Java","C","C++","JavaScript"]

l.clear()
print(l)

# 10


students = ["Anu", "Rahul", "Meera", "Arun", "Diya"]
n = ["Vijay","Sneha"]
students.append("kiran")
students.extend(n)
students.insert(1,"Ravi")


print('No of Rahul in the class room ;',students.count("Ravi"))


students.sort()
students.remove("Rahul")
students.pop()
students.reverse()

print('Finalised List od students attending :',students)

       #No of Rahul in the class room ; 1
       #Finalised List od students attending : ['Vijay', 'Sneha', 'Ravi', 'Meera', 'Diya', 'Arun', 'Anu']

