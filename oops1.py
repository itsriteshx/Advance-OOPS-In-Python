
# SECTION 1: OBJECTS KI BASICS — BUILT-IN CLASSES

# Python mein sab kuch ek object hai
# list, str, int — sab built-in classes ke objects hain
 
print("=== Built-in Class Objects ===")
 
L = [1, 2, 3]
print(type(L))          # <class 'list'>
 
s = str()               # empty string object
print(repr(s))          # ''
 
L2 = list()             # empty list object
print(L2)               # []
 
# Error examples (samajhne ke liye):
# L.upper()      # ERROR — list ka upper() method nahi hota
# s.append('x')  # ERROR — str ka append() method nahi hota
# Har class ke apne specific methods hote hain
 
print()
 
 
# SECTION 2: len() vs .append() — FUNCTION vs METHOD

# len(L)     -> function  -> class ke BAHAR define hai
# L.append() -> method    -> class ke ANDAR define hai
 
print("Function vs Method")
L = [1, 2, 3]
print('len(L) — function :', len(L))
L.append(4)
print('L.append(4) — method:', L)
print()
 
 
# ============================================================
# SECTION 3: CLASS NAMING CONVENTION
# ============================================================
# Python mein class naam PascalCase mein hota hai
# Examples: HelloWorld, BankAccount, SmartPhone, MyClass
 
# Simple class — constructor demo
class Temp:
    def __init__(self):
        print('Temp object created! id:', id(self))
 
print("Constructor Demo")
obj = Temp()
print()

# SECTION 4: ATM CLASS — CONSTRUCTOR & METHODS
# - __init__ ek special (magic) method hai — object bante hi call hota hai
# - self -> current object ka reference
# - Har object ka apna alag id hota hai
 
class Atm:
 
    def __init__(self):
        print('ATM object created. id:', id(self))
        self.pin = ''
        self.balance = 0
 
    def create_pin(self, pin, balance):
        self.pin = pin
        self.balance = balance
        print('PIN created successfully.')
 
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print('PIN changed successfully.')
        else:
            print('Incorrect old PIN. Cannot change.')
 
    def check_balance(self, pin):
        if pin == self.pin:
            print('Your balance is:', self.balance)
        else:
            print('Incorrect PIN.')
 
    def withdraw(self, pin, amount):
        if pin == self.pin:
            if amount <= self.balance:
                self.balance -= amount
                print('Withdrawal successful. Remaining balance:', self.balance)
            else:
                print('Insufficient balance.')
        else:
            print('Incorrect PIN.')
 
 
print("ATM Class Demo")
obj1 = Atm()
obj2 = Atm()
 
# Dono alag objects hain — alag id
print('obj1 id:', id(obj1))
print('obj2 id:', id(obj2))
print('Same object?', id(obj1) == id(obj2))   # False
 
obj1.create_pin('1234', 5000)
obj1.check_balance('1234')
obj1.withdraw('1234', 1500)
obj1.change_pin('1234', '5678')
obj1.check_balance('5678')
print()
 
# SECTION 5: FRACTION CLASS — OPERATOR OVERLOADING
# __str__      -> print() karne par readable output
# __add__      -> + operator override
# __sub__      -> - operator override
# __mul__      -> * operator override
# __truediv__  -> / operator override
 
class Fraction:
 
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator
 
    def __str__(self):
        """print() ke liye readable format"""
        return '{}/{}'.format(self.num, self.den)
 
    def __add__(self, other):
        """fr1 + fr2"""
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)   # string nahi, object return karo
 
    def __sub__(self, other):
        """fr1 - fr2"""
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
 
    def __mul__(self, other):
        """fr1 * fr2"""
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
 
    def __truediv__(self, other):
        """fr1 / fr2"""
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)
 
    def convert_to_decimal(self):
        """Fraction ko decimal mein convert karo"""
        return self.num / self.den
 
 
print("=== Fraction Class — Operator Overloading ===")
fr1 = Fraction(3, 4)
fr2 = Fraction(1, 2)
 
print('fr1 =', fr1)                              # 3/4
print('fr2 =', fr2)                              # 1/2
print('fr1 decimal =', fr1.convert_to_decimal()) # 0.75
 
print('fr1 + fr2 =', fr1 + fr2)   # 3/4 + 1/2 = 10/8
print('fr1 - fr2 =', fr1 - fr2)   # 3/4 - 1/2 = 2/8
print('fr1 * fr2 =', fr1 * fr2)   # 3/4 * 1/2 = 3/8
print('fr1 / fr2 =', fr1 / fr2)   # 3/4 / 1/2 = 6/4
print()
 
# SECTION 6: OPERATOR OVERLOADING — IMPORTANT NOTE
# Har class ke liye + operator ka matlab alag ho sakta hai
# Python decide karta hai ki kaunsa __add__ call karna hai
# based on object type
 
print("Operator Overloading — Different Types")
print('int    + :', 4 + 5)             # addition
print('str    + :', 'hello' + 'world') # concatenation
print('list   + :', [1,2,3] + [4,5])  # list merge
print('Frac   + :', fr1 + fr2)        # fraction addition
 
# set + set nahi hota — sets ka + operator defined nahi hai
# s1 = {1,2,3}
# s2 = {3,4,5}
# s1 + s2   # ERROR: TypeError: unsupported operand type(s) for +: 'set' and 'set'
# Sets ke liye union use karo:
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print('set union (s1 | s2):', s1 | s2)      # {1, 2, 3, 4, 5}
print('set union method   :', s1.union(s2)) # same result
print()
 
 
