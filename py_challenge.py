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
        self.title = "employee"


class Guest:
    def __init__(self, name):
        self.name = name
        self.title = "guest"


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
