from abc import ABC, abstractmethod



class Employee(ABC):
    
    def __init__(self,name,basic_salary):
        self.name = name
        self.__basic_salary = basic_salary

    def retrival_of_salary(self):
        return self.__basic_salary


    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print(f"Employee name {self.name}")
        print(f"Employee Salary {self.__basic_salary}")


class PermanentEmployee(Employee):

    def calculate_salary(self):

        salary = self.retrival_of_salary()
        allowance = salary * 0.20
        return salary + allowance

class ContractEmployee(Employee):

    def calculate_salary(self):

        salary = self.retrival_of_salary()
        allowance = salary * 0.05
        return salary + allowance


# creating objects

employee1 = PermanentEmployee('Gowtham',60000)
employee2 = ContractEmployee('Akash',60000)

employee1.display_details()
print("the salary of the employee is","\n",employee1.calculate_salary())



#2 

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name, number, price_per_day):
        self.name = name
        self.number = number
        self.__price_per_day = price_per_day

    
    def get_rental_price(self):
        return self.__price_per_day

    def display_vehicle_details(self):
        print(f"Vehicle Name: {self.name}")
        print(f"Plate Number: {self.number}")
        print(f"Rental Price per Day: ₹{self.__price_per_day}")

    @abstractmethod
    def calculate_rent(self, days):
        pass



class Car(Vehicle):
    
    def calculate_rent(self, days):
        total_rent = (self.get_rental_price() * days) + 500
        return total_rent



class Bike(Vehicle):
    
    def calculate_rent(self, days):
        total_rent = (self.get_rental_price() * days) + 100
        return total_rent



car1 = Car("Toyota Innova", "KL-34-f-9224", 2000)
bike1 = Bike("Royal Enfield Classic 350", "KL-05-AB-9876", 800)

print("--- Car Rental Details ---")
print("****************************************")
car1.display_vehicle_details()
car_rent = car1.calculate_rent(3)
print(f"Final Rental Amount for 3 days: ₹{car_rent}\n")

print("--- Bike Rental Details ---")
print("******************************************")
bike1.display_vehicle_details()
bike_rent = bike1.calculate_rent(3)
print(f"Final Rental Amount for 3 days: ₹{bike_rent}")