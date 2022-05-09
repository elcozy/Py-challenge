class Person:
    # default value must be at the end if others dont have default
    def __init__(self, name="Jane Doe", age=30, gender="female"):
        self.name = name
        self.age = age
        self.gender = gender

# how to change age to default 0 when creating new instance, without changing the code?
    @classmethod  # here you dont need self. self will require to initialize an instance, but here wit class method you dont need an instance
    # cls to pass the methods defined in the class
    def create_newborn(cls, name, gender):
        return cls(name, 0, gender)

# you can use @staticmethod since you dont need instance variables. this will work with Person.getgoal and john.get_goal()
    def get_goal(self):
        print("My goal is: Live for the moment!")

    def introduce(self):
        print(f"Hi, I'm {self.name}, a {self.age} year old {self.gender}.")


class Student(Person):
    def __init__(self, name, age, gender, previous_organization, skipped_days):
        # super returns with parent class,no need self here this is temporary object of super class(?)
        super().__init__(name, age, gender)
        # Person.__init__(self,name,age,gender) # use super so you dont need to know the parent class (no need to hardcode/explicitly state the
        # parent class so its better practice, more reusable
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days

    @staticmethod
    def get_goal():
        print("Be a junior software developer.")

    def introduce(self):
        print(f"Hi, I'm {self.name}, a {self.age} year old {self.gender} from {self.previous_organization} who skipped {self.skipped_days} "
              f"days from the course already.")

    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days


class Mentor(Person):
    __accepted_levels = ["senior", "junior", "intermediate"]

    def __init__(self, name, age, gender, level):
        super().__init__(name, age, gender)
        self.level = level  # must be in junior / intermediate / senior
        # why does this not have underscore??

    @property
    def level(self):
        return self._level
    # this needs underscore to distinguish it from self.level ; if not, then it will loop (this is not for protection)

    @level.setter
    def level(self, value):
        if value in Mentor.__accepted_levels:
            # ["junior", "senior", "intermediate"]: #better to use in instead of not in
            # the list is hardcoded, create  a variable for this (this is class property for class mentor, better to set it at the
            # start of the class
            self._level = value
        else:
            raise ValueError("blah blah")

    @staticmethod
    def get_goal():
        print("Educate brilliant junior software developers.")

    def introduce(self):
        print(
            f"Hi, I'm {self.name}, a {self.age} year old {self.gender} {self.level} mentor")


class Sponsor(Person):
    def __init__(self, name, age, gender, company, hired_students):
        super().__init__(name, age, gender)
        self.company = company
        self.hired_students = hired_students

    @staticmethod
    def get_goal():
        print("Hire brilliant junior software developers.")

    def introduce(self):
        print(f"Hi, I'm {self.name}, a {self.age} year old {self.gender} who represents {self.company} and hired {self.hired_students} "
              f"students so far.")

    def hire(self):
        self.hired_students += 1


class Cohort(Student):
    def __init__(self, name):
        self.name = name
        self.students = []
        self.mentors = []

    def add_student(self, Student):
        self.students.append(Student)

    def add_mentor(self, Mentor):
        self.mentors.append(Mentor)

    def info(self):
        print(
            f"The {self.name} cohort has {len(self.students)} students and {len(self.mentors)} mentors.")


john = Person("John", 40, "male")
john.get_goal()
john.introduce()
# self represents the instance john so it is automatically called when we call function get_goal, so we dont need to pass it in again)
# to call the class method
rambo = Person.create_newborn("rambo", "male")
rambo.introduce()

jane = Mentor("jane", 18, "female", "senior")
jane.introduce()


# New Task here

print("-----------------------------")

# Write a program that is capable of handling simple restaurants!

# These restaurants have only one product: menu. Different restaurants can have different prices for their menus.

# We’d like to create a new restaurant in the program by giving the name of the restaurant and the price of the menu there.

# The restaurants give a discount to their employees, they get a menu for half price, while a guest needs to pay the full price.

# The restaurants can sit customers at tables (without limitations) and can serve menus to all the current customers. Whenever a menu is served, the customer pays, which is added to the income of the restaurant, and the customer also stands up from the table.

# Using your solution, the following code should run without errors and print the expected results.


# john = Employee('John')
# jane = Guest('Jane')
# restaurant = Restaurant('Galactica', 10)
# print(restaurant) # should print: Galactica | 0 customers | menu for 10$ | income: 0
# restaurant.sit(john, jane)
# print(restaurant) # should print: Galactica | 2 customers | menu for 10$ | income: 0
# restaurant.serve_menu() # should print: John is eating for 5.0\nJane is eating for 10
# print(restaurant) # should print: Galactica | 0 customers | menu for 10$ | income: 15


class Employee:
    def __init__(self, name):
        self.name = name


class Guest:
    def __init__(self, name):
        self.name = name


class Restaurant:
    # default value must be at the end if others dont have default
    def __init__(self, restaurant_name, menu_cost):
        self.restaurant_name = restaurant_name
        self.menu_cost = menu_cost
        self.customers = []
        self.income = 0

    def __str__(self):
        return f'{self.restaurant_name} | {len(self.customers)} customers | menu for {self.menu_cost}$ | income: {self.income}'

    def sit(self, *args):
        z = 1
        for cu in args:
            if isinstance(cu, Employee):
                self.customers.append(
                    {'customer': cu.name, 'cost': self.menu_cost / 2})
                self.income += self.menu_cost / 2
            if isinstance(cu, Guest):
                self.customers.append(
                    {'customer': cu.name, 'cost': self.menu_cost})
                self.income += self.menu_cost

            else:
                "Unexpected error occured"

    def serve_menu(self):
        for cus in self.customers:
            print(f"{cus['customer']} is eating for {cus['cost']}")
        self.customers.clear()
        # print('John is eating for 5.0\nJane is eating for 10')
        pass


john = Employee('John')
jane = Guest('Jane')
restaurant = Restaurant('Galactica', 10)
print(restaurant)  # should print: Galactica | 0 customers | menu for 10$ | income: 0
restaurant.sit(john, jane)
print(restaurant)  # should print: Galactica | 2 customers | menu for 10$ | income: 0
restaurant.serve_menu()  # should print: John is eating for 5.0\nJane is eating for 10
# should print: Galactica | 0 customers | menu for 10$ | income: 15
print(restaurant)

print("-----------------------------")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog1 = Dog('Furkesz', 5)
dog2 = Dog('Furkesz', 5)
dog2 = dog1
print(dog1 == dog2)

print("-----------------------------")


# Write a program that is capable of managing flats and residents. We want to register new residents by their names. We want to register new flats by the unique id of the flat and a limit for the maximum number of residents who can live in the flat. We want to add resdidents to the flats and also remove residents by their names.

# Using your solution, the following code should run without errors and print the expected results.

class Resident:
    def __init__(self, name):
        self.name = name


class Flat:
    def __init__(self, flat_id, flat_limit):
        self.flat_id = flat_id
        self.flat_limit = flat_limit
        self.number_residents = 0
        self.flat_occupants = []

    def __str__(self):
        return f'{self.flat_id} has {self.number_residents} residents'

    def add(self, occupant):

        if self.number_residents < self.flat_limit:
            self.flat_occupants.append(occupant.name)
            self.number_residents += 1
        else:
            print('The flat is full.')

    def remove(self, name):
        if name in self.flat_occupants:
            self.flat_occupants.remove(name)
            self.number_residents -= 1


flat1 = Flat('FLT1', 3)
jane = Resident('Jane')
john = Resident('John')
kate = Resident('Kate')
kyle = Resident('Kyle')
flat1.add(jane)
flat1.add(john)
flat1.add(kate)
print(flat1)  # should print: FLT1 flat has 3 residents.
flat1.add(kyle)  # should print: The flat is full.
print(flat1)  # should print: FLT1 flat has 3 residents.
flat1.remove('Jane')
print(flat1)  # should print: FLT1 flat has 2 residents.
flat1.remove('Jane')
print(flat1)  # should print: FLT1 flat has 2 residents.


print("-----------------------------")

# What is the output of the following program? Explain your answer!


class CreditCard:
    def __init__(self, provider, transaction_fee, balance=0):
        self.provider = provider
        self.transaction_fee = transaction_fee
        self.balance = balance

    def withdraw(self, amount):
       fee = amount * self.transaction_fee
       if amount + fee > self.balance:
           print('Not enough credit.')
           return  0
       self.balance -= amount + fee
       return amount
 
class MasterCard(CreditCard):
    def __init__(self, balance):
        super().__init__('MasterCard', 0.01, balance)
 
class Visa(CreditCard):
    def __init__(self, balance):
        super().__init__('Visa', 0.02, balance)
 
    def withdraw(self, amount):
        if (amount > self.balance):
            print('Not enough credit.')
            return 0
        self.balance -= amount
        return amount
 
master_card = MasterCard(1000)
visa = Visa(1000)
cash = master_card.withdraw(100) + visa.withdraw(100)
balance = master_card.balance + visa.balance
print(cash, balance)

# The output is 200 1799.0



# EXPLANATION :


# The cash is 200 because in the master_card.withdraw(100) = 100 and the visa.withdraw(100) gives the same 100

# this is because they did not meet the condition in the conditional statements in the method method

# In the child class called MasterCard and Visa,  default values (provider, transaction_fee values) were passed up to parent.

# the balance is 1799.0  is because

# master_card.balance ---- 899.0 ---> because 1000 (passed to Mastercard class) -  101.0 (amount + fee) in the withdraw method
# In the Visa class, the method called withdrawal was overwritten from the one inherited from the parent class CreditCard.
# visa.balance --- 900 ----> because  1000 - 100( from the method of Visa class - 100(passed to withdraw method of Visa class))

# That is the reason for the result


print("-----------------------------")

class Car:
   def __init__(self, consumption, fuel = 0):
       self.consumption = consumption
       self.fuel = fuel
 
   def ride(self, km):
       required_fuel = km * (self.consumption / 100)
       kms_left = km - (self.fuel / required_fuel) * km
       self.fuel = max(self.fuel - required_fuel, 0)
       return kms_left
 
class PetrolCar(Car):
   def __init__(self, consumption, fuel):
       super().__init__(consumption, fuel)
 
class PetrolElectricHybridCar(Car):
   def __init__(self, consumption, fuel, kms_with_electric_engine):
       super().__init__(consumption, fuel)
       self.kms_with_electric_engine = kms_with_electric_engine
 
   def ride(self, km):
       kms_left_with_petrol = super().ride(km)
       kms_left = max(kms_left_with_petrol - self.kms_with_electric_engine, 0)
       return kms_left
 
petrol_car = PetrolCar(10, 50)
hybrid_car = PetrolElectricHybridCar(10, 50, 100)
 
print(petrol_car.ride(550))
print(hybrid_car.ride(550))

# The output is 

# 50.0

# 0

# REASON FOR RESULT

# The first result 50 is gotten from 

# petrol_car = PetrolCar(10, 50) and print(petrol_car.ride(550))
# The child class Petrol class passed up the comsumption and the fuel
# In the parent method the ride returns Kms_left which is gotten from
#        required_fuel = 550 * (10/ 100)
#        kms_left = km - (50 / required_fuel) * 550
# That resulted in 50.0

# Second result = 0

# Reason is that the method ride has be overridded by the class 
# PetrolElectricHybridCar()
# and it goes like 
#        kms_left_with_petrol = super().ride(km)
#        kms_left = max(kms_left_with_petrol - self.kms_with_electric_engine, 0)
#        return kms_left
#   the super().ride(km) inherits the initial ride method created in the parent class.. so that resulted in
#  required_fuel = 550 * (10/ 100)
#  kms_left = km - (50 / required_fuel) * 550 = 50
# then self.fuel = max(self.fuel - 550 * (10/ 100), 0) == the maximum from -5 and 0 = 0
# so the class hybridclass returns 0 which is the km_left{kms_left === max(kms_left_with_petrol - self.kms_with_electric_engine, 0)} = 
#  max(0 - 100, 0)} = which gives 0 as the max number here







