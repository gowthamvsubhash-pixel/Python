

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age


# class Employee(Person):
#     def __init__(self,name,age,employee_id,salary,join_date):
#         super().__init__(name,age)
#         self.employee_id = employee_id
#         self.salary = salary
#         self.join_date = join_date

#     def display_details(self):
#         print(self.name)
#         print(self.age)
#         print(self.employee_id)
#         print(self.salary)
#         print(self.join_date)
    

# class Father(Person):
#     def __init__(self,name,age,no_of_children):
#         self.no_of_children = no_of_children
#     def display_details(self):
#         print(self.name)
#         print(self.age)
#         print(self.no_of_children)
    

# class Son(Person):
#     def __init__(self,name,age,father_name):
#         super().__init__(name,age)
#         self.father_name = father_name
#     def display_details(self):
#         print(self.name)
#         print(self.age)
#         print(self.father_name)


# class Husband(Person):
#     def __init__(self,name,age,wife_name,date_of_marry):
#         super().__init__(name,age)
#         self.wife_name = wife_name
#         self.date_of_marry = date_of_marry

#     def display_details(self):
#         print(self.name)
#         print(self.age)
#         print(self.date_of_marry)
#         print(self.wife_name)



# per = Person('Steve',34)

# emp = Employee('gg',23,'Emp1',20000,'23-6-2009')
# emp.display_details()
# hus = Husband('thor',32,'meera','23-6-2000')
# hus.display_details()



# ---------------------------------------------------------

class Employee():
    def calculate_salary(self):
        print('Calculate Salary')
    

class FulltimeEmployee(Employee):
    def calculate_salary(self):
        print('\nFull time employee recieves a fixed amount monthly\n')


class ParttimeEmployee(Employee):
    def calculate_salary(self):
        print('Part time employee salary is based on working hours\n')


class Freelancer(Employee):
    def calculate_salary(self):
        print('Freelancer Salary is based on completed project\n')


full = FulltimeEmployee()
full.calculate_salary()

part = ParttimeEmployee()
part.calculate_salary()

free = Freelancer()
free.calculate_salary()