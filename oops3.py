
# SECTION 1: CLASS RELATIONSHIPS

# 1. Aggregation  (Has-A relationship)
# 2. Inheritance  (Is-A relationship)
# 1. AGGREGATION (Has-A Relationship)


# Ek class doosri class ka object apne andar rakhti hai
class Address:

    def __init__(self, city, pin, state):
        self.__city = city   # private attribute
        self.pin = pin
        self.state = state

    def get_city(self):
        return self.__city

    def edit_address(self, new_city, new_pin, new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state


class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address   # Address object yahan aggregate ho raha hai

    def print_address(self):
        # Private attribute ko class ke bahar access karne ke 2 tarike:
        # 1. getter method: self.address.get_city()
        # 2. name mangling:  self.address._Address__city
        print(self.address.get_city(), self.address.pin, self.address.state)

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.edit_address(new_city, new_pin, new_state)


# --- Aggregation Demo ---
add1 = Address('Gurgaon', 122011, 'Haryana')
cust = Customer('Nitish', 'Male', add1)

print("=== Aggregation Demo ===")
cust.print_address()                                      # Gurgaon 122011 Haryana
cust.edit_profile('Ankit', 'Mumbai', 111111, 'Maharashtra')
cust.print_address()                                      # Mumbai 111111 Maharashtra
print()



# SECTION 2: INHERITANCE (Is-A Relationship)

# Child class parent class ki properties aur methods inherit karti hai
# Benefits: Code Reuse, Extensibility

# 2a. Basic Inheritance Example


class User:
    """Parent Class"""

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def login(self):
        print(f'{self.name} logged in.')


class Student(User):
    """Child Class — User se inherit kar raha hai"""

    def __init__(self, name, gender, rollno):
        super().__init__(name, gender)   # Parent ka constructor call
        self.rollno = rollno

    def enroll(self):
        print(f'{self.name} enrolled into the course. Roll No: {self.rollno}')


print("=== Basic Inheritance Demo ===")
s = Student('Ritesh', 'Male', 101)
s.login()     # parent ka method
s.enroll()    # child ka method
print()


# 2b. What Gets Inherited?
#     - Constructor (agar child ka apna na ho)
#     - Non-Private Attributes
#     - Non-Private Methods
#     - Private attributes DIRECTLY accessible NAHI hote


class Phone:

    def __init__(self, price, brand, camera):
        self.__price = price   # private — child directly access nahi kar sakta
        self.brand = brand
        self.camera = camera

    def buy(self):
        print(f'Buying {self.brand} phone.')

    def show_price(self):
        print(f'Price: {self.__price}')   # parent hi apna private access kar sakta hai


class SmartPhone(Phone):

    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera)   # parent constructor call
        self.os = os
        self.ram = ram

    def specs(self):
        print(f'OS: {self.os}, RAM: {self.ram}GB')
        # self.__price  <-- YE ERROR DEGA (private attribute)
        # self.show_price() <-- Ye chalega (parent ka public method)


print("Inheritance — What gets inherited")
s = SmartPhone(20000, 'Samsung', 12, 'Android', 8)
s.buy()          # inherited
s.show_price()   # inherited
s.specs()        # child ka apna
print()



# 2c. Method Overriding
#     Child class parent ke method ko apne tarike se define kare

class BasicPhone:

    def buy(self):
        print('Buying a Basic Phone.')


class AdvancedPhone(BasicPhone):

    def buy(self):  # Override kar diya parent ka buy()
        print('Buying an Advanced SmartPhone.')


print("=== Method Overriding ===")
obj = AdvancedPhone()
obj.buy()   # Child ka method chalega
print()

# 2d. super() Keyword
#     Parent class ke methods aur constructor ko call karne ke liye

class LandlinePhone:

    def __init__(self, brand):
        self.brand = brand

    def call(self):
        print(f'{self.brand}: Making a call from landline.')


class CordlessPhone(LandlinePhone):

    def __init__(self, brand, range_meters):
        super().__init__(brand)          # parent ka __init__ call
        self.range_meters = range_meters

    def call(self):
        super().call()                   # parent ka call() bhi chalao
        print(f'Range: {self.range_meters} meters (cordless)')


print("=== super() Demo ===")
c = CordlessPhone('Panasonic', 50)
c.call()
print()

# SECTION 3: TYPES OF INHERITANCE
# 3a. Single Inheritance  —  A -> B

class Animal:
    def breathe(self):
        print('Breathing...')

class Dog(Animal):
    def bark(self):
        print('Woof!')

print("=== Single Inheritance ===")
Dog().breathe()
Dog().bark()
print()

# 3b. Multilevel Inheritance  —  A -> B -> C

class LivingBeing:
    def exist(self):
        print('I exist.')

class Mammal(LivingBeing):
    def warm_blood(self):
        print('I am warm-blooded.')

class Human(Mammal):
    def think(self):
        print('I can think.')

print("Multilevel Inheritance")
h = Human()
h.exist()        # LivingBeing se
h.warm_blood()   # Mammal se
h.think()        # Human ka apna
print()

# 3c. Hierarchical Inheritance  —  A -> B, A -> C
class Vehicle:
    def move(self):
        print('Vehicle is moving.')

class Car(Vehicle):
    def drive(self):
        print('Driving a car.')

class Bike(Vehicle):
    def ride(self):
        print('Riding a bike.')

print("Hierarchical Inheritance")
Car().move()
Bike().move()
print()

# 3d. Multiple Inheritance  —  A, B -> C
class Camera:
    def click_photo(self):
        print('Clicking photo.')

class GPS:
    def navigate(self):
        print('Navigating with GPS.')

class ModernPhone(Camera, GPS):
    pass

print("=== Multiple Inheritance ===")
mp = ModernPhone()
mp.click_photo()
mp.navigate()
print()

# 3e. Diamond Problem & MRO (Method Resolution Order)
#     Python MRO follow karta hai C3 Linearization algorithm
#     MRO dekhne ke liye: ClassName.__mro__
class A:
    def hello(self):
        print('Hello from A')

class B(A):
    def hello(self):
        print('Hello from B')

class C(A):
    def hello(self):
        print('Hello from C')

class D(B, C):   # Diamond shape
    pass

print("=== Diamond Problem (MRO) ===")
D().hello()                    # B ka chalega (MRO order: D -> B -> C -> A)
print('MRO:', [cls.__name__ for cls in D.__mro__])
print()

# SECTION 4: POLYMORPHISM
# Ek hi naam, alag alag behavior
# 4a. Method Overriding (Runtime Polymorphism)

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

print("Polymorphism — Method Overriding")
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f'{shape.__class__.__name__} area: {shape.area()}')
print()

# 4b. Method Overloading (Default Arguments se simulate karte hain)
#     Python natively support nahi karta, default params use karo
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

print("Polymorphism — Method Overloading (simulated)")
calc = Calculator()
print(calc.add(5))
print(calc.add(5, 10))
print(calc.add(5, 10, 15))
print()


# 4c. Operator Overloading
#     __add__, __str__, __len__ jaisi dunder methods override karo
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):   # + operator override
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):          # print ke liye readable output
        return f'Vector({self.x}, {self.y})'

print("=== Polymorphism — Operator Overloading ===")
v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)   # Vector(6, 8)
print()


# SECTION 5: ABSTRACTION
# Implementation details chupaao, sirf interface dikhao
# Abstract class directly instantiate NAHI ho sakti

from abc import ABC, abstractmethod

class BankApp(ABC):
    """Abstract Base Class — blueprint hai, directly use nahi hogi"""

    def database(self):
        print('Connected to database.')   # concrete method

    @abstractmethod
    def security(self):
        pass   # child ko implement KARNA hi hoga

    @abstractmethod
    def display(self):
        pass   # child ko implement KARNA hi hoga


class MobileApp(BankApp):
    """Concrete class — saare abstract methods implement kiye"""

    def security(self):
        print('Mobile OTP Security enabled.')

    def display(self):
        print('Displaying Mobile Banking Dashboard.')

    def mobile_login(self):
        print('Logged in via Mobile App.')


class WebApp(BankApp):
    """Ek aur concrete class"""

    def security(self):
        print('Web 2FA Security enabled.')

    def display(self):
        print('Displaying Web Banking Portal.')


print("Abstraction Demo")
mob = MobileApp()
mob.database()      # inherited concrete method
mob.security()      # apna implementation
mob.display()
mob.mobile_login()
print()

web = WebApp()
web.database()
web.security()
web.display()
print()

# BankApp() directly banane ki koshish karo toh error aayega:
# obj = BankApp()  -->  TypeError: Can't instantiate abstract class

