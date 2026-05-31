
# ============================================================
# SECTION 1: OOP PRACTICAL — 2D COORDINATES & LINES
# ============================================================
# Features:
#   - 2D Point create aur view karo
#   - 2 points ke beech distance nikalo
#   - Origin se distance nikalo
#   - Check karo koi point kisi line par hai ya nahi
#   - Point aur Line ke beech shortest distance nikalo
 
class Point:
 
    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y
 
    def __str__(self):
        return '<{}, {}>'.format(self.x_cod, self.y_cod)
 
    def euclidean_distance(self, other):
        """Do points ke beech Euclidean distance"""
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2) ** 0.5
 
    def distance_from_origin(self):
        """Origin (0,0) se distance"""
        return (self.x_cod**2 + self.y_cod**2) ** 0.5
        # Alternate: return self.euclidean_distance(Point(0, 0))
 
 
class Line:
 
    def __init__(self, A, B, C):
        # Line equation: Ax + By + C = 0
        self.A = A
        self.B = B
        self.C = C
 
    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A, self.B, self.C)
 
    def point_on_line(self, point):
        """Check karo point line par hai ya nahi"""
        if self.A * point.x_cod + self.B * point.y_cod + self.C == 0:
            return '{} lies on the line'.format(point)
        else:
            return '{} does not lie on the line'.format(point)
 
    def shortest_distance(self, point):
        """Point aur line ke beech shortest (perpendicular) distance"""
        return abs(self.A * point.x_cod + self.B * point.y_cod + self.C) / \
               (self.A**2 + self.B**2) ** 0.5
 
 
# --- Demo ---
print("=== 2D Geometry Demo ===")
 
p1 = Point(1, 10)
p2 = Point(4, 6)
l1 = Line(1, 1, -2)
 
print('Point 1:', p1)
print('Point 2:', p2)
print('Line   :', l1)
print('Distance between p1 and p2:', round(p1.euclidean_distance(p2), 4))
print('Distance of p1 from origin :', round(p1.distance_from_origin(), 4))
print('Point on line check        :', l1.point_on_line(p1))
print('Shortest distance (p1-line):', round(l1.shortest_distance(p1), 4))
print()
 
 
# ============================================================
# SECTION 2: HOW OBJECTS ACCESS ATTRIBUTES & METHODS
# ============================================================
 
class Person:
 
    def __init__(self, name, country):
        self.name = name
        self.country = country
 
    def greet(self):
        if self.country == 'india':
            print('Namaste,', self.name)
        else:
            print('Hello,', self.name)
 
 
print("=== Object Attribute & Method Access ===")
p = Person('Ritesh', 'india')
print('Name:', p.name)          # attribute access
p.greet()                        # method access
 
# Attribute outside class se bhi add ho sakta hai (dynamic)
p.gender = 'male'
print('Gender (added outside):', p.gender)
print()
 
 
# ============================================================
# SECTION 3: REFERENCE VARIABLES
# ============================================================
# - Reference variable object ko hold karti hai
# - Ek object ke multiple references ho sakte hain
# - Naya reference banana = naya object NAHI banta
 
class PersonRef:
 
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
 
 
print("=== Reference Variables ===")
p = PersonRef('Nitish', 'male')
q = p   # dono same object ko point kar rahe hain
 
print('id(p):', id(p))
print('id(q):', id(q))   # same id — same object
 
# q se change karo toh p mein bhi dikhega
q.name = 'Ankit'
print('p.name after q.name change:', p.name)   # Ankit
print()
 
 
# ============================================================
# SECTION 4: PASS BY REFERENCE
# ============================================================
# Objects function mein reference se pass hote hain
# Matlab function ke andar change karo toh bahar bhi dikhega
 
class PersonPass:
 
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
 
 
def greet_and_modify(person):
    print('Inside function — id:', id(person))
    person.name = 'Ankit'   # original object modify ho gaya
 
 
print("=== Pass by Reference ===")
p = PersonPass('Nitish', 'male')
print('Before — p.name:', p.name)
print('Before — id(p)  :', id(p))
greet_and_modify(p)
print('After  — p.name:', p.name)   # Ankit (modified)
print()
 
 
# ============================================================
# SECTION 5: OBJECT MUTABILITY
# ============================================================
# Object mutable hote hain — function return karne par bhi same object rehta hai
 
class PersonMut:
 
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
 
 
def modify(person):
    person.name = 'Ankit'
    return person
 
 
print("=== Object Mutability ===")
p = PersonMut('Nitish', 'male')
p1 = modify(p)
print('id(p) == id(p1):', id(p) == id(p1))   # True — same object
print('p.name :', p.name)
print('p1.name:', p1.name)
print()
 
 
# ============================================================
# SECTION 6: ENCAPSULATION
# ============================================================
# Data aur methods ko ek saath wrap karna
# Private attributes __ se banate hain — bahar directly access nahi hote
# Getters aur Setters se controlled access dete hain
 
class Atm:
 
    def __init__(self):
        self.pin = ''
        self.__balance = 0   # private attribute
 
    # Getter
    def get_balance(self):
        return self.__balance
 
    # Setter — type check ke saath
    def set_balance(self, new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print('Invalid input! Balance must be an integer.')
 
    def create_pin(self, pin, balance):
        self.pin = pin
        self.__balance = balance
        print('PIN created successfully.')
 
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print('PIN changed successfully.')
        else:
            print('Incorrect old PIN.')
 
    def check_balance(self, pin):
        if pin == self.pin:
            print('Your balance is:', self.__balance)
        else:
            print('Incorrect PIN.')
 
    def withdraw(self, pin, amount):
        if pin == self.pin:
            if amount <= self.__balance:
                self.__balance -= amount
                print('Withdrawal successful. Remaining balance:', self.__balance)
            else:
                print('Insufficient balance.')
        else:
            print('Incorrect PIN.')
 
 
print("=== Encapsulation — ATM Demo ===")
atm = Atm()
atm.create_pin('1234', 5000)
atm.check_balance('1234')
atm.withdraw('1234', 1000)
atm.set_balance(10000)
print('Balance via getter:', atm.get_balance())
atm.set_balance('abc')   # invalid input
print()
 
 
# ============================================================
# SECTION 7: COLLECTION OF OBJECTS
# ============================================================
# Objects ko list ya dict mein store kar sakte hain
 
class PersonCol:
 
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
 
 
p1 = PersonCol('Nitish', 'male')
p2 = PersonCol('Ankit', 'male')
p3 = PersonCol('Ankita', 'female')
 
print("=== Collection of Objects — List ===")
person_list = [p1, p2, p3]
for person in person_list:
    print(person.name, '-', person.gender)
print()
 
print("=== Collection of Objects — Dict ===")
person_dict = {'p1': p1, 'p2': p2, 'p3': p3}
for key in person_dict:
    print(key, '->', person_dict[key].name, '|', person_dict[key].gender)
print()
 
 
# ============================================================
# SECTION 8: STATIC VARIABLES & STATIC METHODS
# ============================================================
# Static (Class-level) Variables:
#   - Class level par define hoti hain
#   - ClassName.var se access hoti hain
#   - Saare objects ke beech SHARED hoti hain
#   - Object ke bina bhi access kar sakte hain
#
# Static Methods:
#   - @staticmethod decorator se banate hain
#   - self ya cls parameter nahi hota
#   - Utility functions ke liye use hota hai
 
class AtmStatic:
 
    __counter = 1   # static (class-level) variable — shared among all objects
 
    def __init__(self):
        self.pin = ''
        self.__balance = 0
        self.cid = AtmStatic.__counter       # har object ka unique ID
        AtmStatic.__counter += 1
 
    @staticmethod
    def get_counter():
        """Kitne ATM objects bane hain — static method"""
        return AtmStatic.__counter - 1
 
 
print("=== Static Variables & Methods — ATM Counter ===")
atm1 = AtmStatic()
atm2 = AtmStatic()
atm3 = AtmStatic()
 
print('ATM 1 ID:', atm1.cid)
print('ATM 2 ID:', atm2.cid)
print('ATM 3 ID:', atm3.cid)
print('Total ATMs created:', AtmStatic.get_counter())
print()
 
 
# ============================================================
# SECTION 9: STATIC VARIABLE — REAL WORLD EXAMPLE
# ============================================================
 
class Lion:
 
    __water_source = 'Well in the Circus'   # shared static variable
 
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
 
    def drinks_water(self):
        print(self.__name, 'drinks water from the', Lion.__water_source)
 
    @staticmethod
    def get_water_source():
        return Lion.__water_source
 
 
print("=== Static Variable — Lion Example ===")
simba = Lion('Simba', 'Male')
mufasa = Lion('Mufasa', 'Male')
 
simba.drinks_water()
mufasa.drinks_water()
print('Water source (class level):', Lion.get_water_source())
print()
 
 

