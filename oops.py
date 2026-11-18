# --------- OOPS - object oriented programming language ---------

# # Data management 

std_name1 = 'Vishnu'
age_1 = 21

std_name2 = 'Aakash'
age_2 = 21

std_name3 = 'Jerin'
age_3 = 24

std_name4 = 'Ajith'
age_4 = 22

std_name5 = 'Arjun'
age_5 = 22

print('std_name :',std_name1)
print('age :',age_1,'\n')
print('std_name :',std_name2)
print('age :',age_2,'\n')
print('std_name :',std_name3)
print('age :',age_3,'\n')
print('std_name :',std_name4)
print('age :',age_4,'\n')
print('std_name :',std_name5)
print('age :',age_5,'\n')



# class 
print('\tClass Student')
print(' ')
class Student:
    def __init__(self , name , age):
        self.name= name
        self.age= age

std_1 = Student('Vishnu',21)
std_2 = Student('Aakash',21)
std_3 = Student('Dhanesh',26)
std_4 = Student('Abhinav',25)
std_5 = Student('Ajith',22)

print(std_1.name,std_1.age)
print(std_2.name,std_2.age)
print(std_3.name,std_3.age)
print(std_4.name,std_4.age)
print(std_5.name,std_5.age)
print(' ')


# Book class
print('\tClass Book')
print(' ')
class Book:
    def __init__(self, book_name , author , year):
        self.name= book_name
        self.author = author
        self.year = year

book1 = Book('Balarama','Vishnu',2026)
book2 = Book('Kalikudukka','Aakash',2026)
book3 = Book('Artham ','Dhamuu',2016)
book4 = Book('Chuvadd','Bheem',2020)
book5 = Book('Orikkal','OV Vijayan',1999)

print(f'Book Name : {book1.name}\t\tAuthor :{book1.author}\t\tYear :{book1.year}')
print(f'Book Name : {book2.name}\t\tAuthor :{book2.author}\t\tYear :{book2.year}')
print(f'Book Name : {book3.name}\t\tAuthor :{book3.author}\t\tYear :{book3.year}')
print(f'Book Name : {book4.name}\t\tAuthor :{book4.author}\t\tYear :{book4.year}')
print(f'Book Name : {book5.name}\t\tAuthor :{book5.author}\tYear :{book5.year}')
print(' ')

# Class Attribute
# Instance Attribute



print('\tClass Employee')
print(' ')
# defining class Employee - getting name , id , role , exp and salary 
class Employee:
    # class attribute(s) declaring
    nation = 'India'  # used to store any constant or common values .
    def __init__(self,name,emp_id,role,experience,salary):
        self.name = name 
        self.id = emp_id
        self.role = role
        self.experience = experience
        self.salary = salary
    # create a function to display the details instead of print all details manually
    def display_details(self):
        print(f'Name : {self.name}\nID : {self.id}\nRole : {self.role}\nExperience : {self.experience}\nSalary : {self.salary}\n')

# inside a class if there is a function that is a method . used to call when needed  . For code reusabilty 


emp_1 = Employee('Vishnu','EMP1','WD',2,20000)
emp_2 = Employee('Bheem','EMP2','DS',1,42000)
emp_3 = Employee('Ben10','EMP3','FSD',0,25000)
emp_4 = Employee('Krish','EMP4','SD',5,70000)
emp_5 = Employee('Bahubali','EMP5','Python D',12,90000)

emp_1.display_details()
emp_2.display_details()
emp_3.display_details()
emp_4.display_details()
emp_5.display_details()


# accessing class attribute 
print('Nationality :',Employee.nation,'\n')

# -----------------------------------------------------------------------------------------------------------------

print(' ')
print('Manual print without function - method')
print(' ')

print(f'Name : {emp_1.name}\t\t Emp_ID : {emp_1.id}\t\t Role : {emp_1.role}\t\t Experience : {emp_1.experience}\t\t Salary : {emp_1.salary}')
print(f'Name : {emp_2.name}\t\t Emp_ID : {emp_2.id}\t\t Role : {emp_2.role}\t\t Experience : {emp_2.experience}\t\t Salary : {emp_2.salary}')
print(f'Name : {emp_3.name}\t\t Emp_ID : {emp_3.id}\t\t Role : {emp_3.role}\t\t Experience : {emp_3.experience}\t\t Salary : {emp_3.salary}')
print(f'Name : {emp_4.name}\t\t Emp_ID : {emp_4.id}\t\t Role : {emp_4.role}\t\t Experience : {emp_4.experience}\t\t Salary : {emp_4.salary}')
print(f'Name : {emp_5.name}\t\t Emp_ID : {emp_5.id}\t\t Role : {emp_5.role}\t Experience : {emp_5.experience}\t Salary : {emp_5.salary}')

# -----------------------------------------------------------------------------------------------------------------



class Students():
    count = 0
    def __init__(self,name,age,register_number):
        self.name= name
        self.age = age
        self.register_number = register_number

        # increment count by 1
        Students.count = Students.count +1

    def std_count(self):
        print(f'Students Count :{Students.count}')
        # print(f'Name : {self.name}\nAge : {self.age}\nRegister Number : {self.register_number}\n')


std1 = Students('Vishnu',21,32456)
std2 = Students('Bheem',24,45456)
std3 = Students('Krish',25,45789)

std1.std_count()



# Inheritance 

print('Inheritance ')

class Animal:
    def __init__(self,has_leg):
        self.has_leg = has_leg


class Dog(Animal):
    pass

dog = Dog(has_leg='Yes')
print('Dog has 4 legs',dog.has_leg)



#--------------------------------------

class Animal:
    def __init__(self,eat,sleep):
        self.eat = eat
        self.sleep = sleep

class Dog(Animal):
    def __init__(self,eat,sleep):
        super().__init__(eat,sleep)
        self.speak = 'Bow Bow'


class Cat(Animal):
    def __init__(self,eat,sleep):
        super().__init__(eat,sleep)
        self.speak = 'Meow Meow'


dog = Dog(sleep='sleep',eat='eat')
cat = Cat(eat='eat',sleep='sleep')


print(dog.speak,dog.sleep,dog.eat)
print(cat.speak,cat.sleep,cat.eat)


# ----------------------------------------------

# super(). - key is used if we need any attribute from parent class and also need some other attributes seperately then we use super key . or else we dont need to use 
# super() key. 
# eg : if we need name , place from parent class and additionally required age attribute . so in this case we use super() key . otherwise no need of super() key.
# additional attribute is store usually like - self.attributename = 'value'

 
# # ---------- INHERITANCE TASK 1 ----------

def call_all_func():
    dog.display_dog()
    dog.eat()
    dog.bark()
    cat.display_cat()
    cat.eat()
    cat.meow()


class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('The animal is eating')


class Cat(Animal):
    # def __init__(self,name,age):
    #     super().__init__(name,age)

    def display_cat(self):
        print(f'Poocha : {cat.name}\nVayas : {cat.age}')

    def meow(self):
        print('Meow! Meow!\n')

class Dog(Animal):
    # def __init__(self,name,age):
    #     super().__init__(name,age)
        
    def display_dog(self):
        print(f'\nPatti : {dog.name}\nVayas : {dog.age}')

    def bark(self):
        print('Woof! Woof!\n')

dog = Dog(name='Patti Ser',age=2)
cat = Cat(name='Poocha Ser',age=1)


call_all_func()


# ---------- INHERITANCE TASK 2 ----------

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):

        print(f'Name : {person_.name}\nAge : {person_.age}')
    
class Student(Person):

    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course = course
        
    def show_course(self):
        print(f'Course : {self.course}')


person_ = Student('Vi',21,'Data Science')

person_.display()
person_.show_course()



# Abstract Class

from abc import ABC , abstractmethod

class Bank(ABC):

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def loan(self):
        pass

class SBI(Bank):
    def deposit(self):
        print('Deposit Done')
    def loan(self):
        print('Loan Granted')
    def profit(self):
        print('Profit ')

sbi = SBI()
sbi.deposit()
sbi.loan()
sbi.profit()



# -------------------- ABSTRACT METHOD TASK 1 --------------------

from abc import ABC , abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


pi = 3.14

class Rectangle(Shape):

    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        rectangle_area = self.length * self.width
        print(f'Rectangle Area : {rectangle_area}')
        
    

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        circle_area = pi * self.radius * self.radius
        print(f'Circle Area : {circle_area}')

rect = Rectangle(5,3)
rect.area()
circ = Circle(2)
circ.area()