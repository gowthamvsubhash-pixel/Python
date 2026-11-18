# Encapsulation



# class BankAccount:
#     def __init__(self,owner_name,bank_balance,account_type):
#         self.owner_name = owner_name
#         self.__bank_balance = bank_balance                                      # private member
#         self._account_type = account_type                                       # protected member
    
#     # access private members using @property by returning the value
#     @property
#     def bank_bal(self):
#         return self.__bank_balance                                     

#     # access protected members using @property by returning the value
#     @property
#     def acc_type(self):
#         return self._account_type

#     # to update the value in private attribute
#     @bank_bal.setter                                # bank.bal is a property 
#     def bank_balance(self,deposit_amt):
#         if deposit_amt <= 0:
#             raise ValueError("Deposit amount cant be zero or negative ")

#         self.__bank_balance += deposit_amt

#     # to update private attribute
#     @acc_type.setter
#     def account_type_change(self,type_acc):
#         # type_acc = type_acc.lower()
#         # if type_acc == 'savings' or type_acc == 'current' :
#         #     self._account_type = type_acc
#         # else :
#         #     print('Account type cannot be empty')
#         if type_acc == '' :
#             raise 'Account type cannot be empty'

        

#         self._account_type = type_acc

# bank = BankAccount('Vishnu',20,'Savings')

# # syntax - class_object.property_classname for eg : bank.acc_type
# print(bank.acc_type)
# print('Initial Balance :',bank.bank_bal)


# bank.bank_balance = 123
# print('After adding setter :',bank.bank_balance)

# bank.account_type_change = 'current'
# print(bank.acc_type)


# # in line - print(bank.bank_bal) - we are not calling the function() but we just using funtion name to get the result . 
# # function calling - bank_bal()
# # the bank_balance is private attribute but we can access the  attribut using @property . the create a function and return that attribute(sels.__bank_balance)
# # then we get the value by print(bank.bank_bal)



# # TASK 2 -------------------

# class Employee:
#     def __init__(self,employee_name,department,salary):
#         self.employee_name = employee_name
#         self._department = department
#         self.__salary = salary

#     @property
#     def get_salary(self):
#         return self.__salary

#     @get_salary.setter
#     def salary_update(self,new_salary):
#         if new_salary<=0:
#             raise "Salary cant be zero or negative "

#         self.__salary = new_salary


# class Manager(Employee):
#     def display_details(self):
#         print(' ')
#         print(f'Public attribute :"{self.employee_name}"')
#         print(f'protected attribute :"{self._department}"\n')


# manager = Manager('Vishnu','Data Science',20000)
# manager.display_details()


# print('Initial Salary : ',manager.get_salary)
# manager.salary_update = 32000
# print('Updated Salary : ',manager.salary_update)


# TASK 3 -------------------


class Vehicle:
    def __init__(self,vehicle_name,rental_type,rental_price):
        self.vehicle_name = vehicle_name
        self._rental_type = rental_type
        self.__rental_price = rental_price
    @property
    def rental_price(self):
        return self.__rental_price

    @rental_price.setter
    def rent_update(self,rent_new):
        if rent_new<=0:
            raise "Rental amount cannot be empty"

        self.__rental_price = rent_new


    def display_details(self):
        print(f'Vehicle name : {self.vehicle_name}')
        print(f'Rental type : {self._rental_type}')




class Car(Vehicle):

    def calculate_rent(self,days):
        return self.rental_price * days

    def display_details(self):
        print(f'Vehicle name : {self.vehicle_name}')
        print(f'Rental type : {self._rental_type}')
        print(f'Rental price per day : {self.rental_price}')



class Bike(Vehicle):

    def calculate_rent(self,days):
        return self.rental_price * days

    def display_details(self):
        print(f'Vehicle name : {self.vehicle_name}')
        print(f'Rental type : {self._rental_type}')
        print(f'Rental price per day : {self.rental_price}')


# vehicle = Bike('Bike','Monthly',5000)
# vehicle.display_details()


car = Car('Car','Day wise ',2000)
bike = Bike('Bike','Day wise',800)


rent_car = car.calculate_rent(5)
rent_bike = bike.calculate_rent(4)

print(' ')
print(f'Car Rent : {rent_car}')
print(f'Bike Rent : {rent_bike}\n')

car.rent_update = 5000
bike.rent_update = 4000
car.display_details()
print('\n')
bike.display_details()
