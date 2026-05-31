# # Class Realtionship 
# # 1)Aggeration=has a relationship 
# rohmbs/rectangle
# class Customer:
#     def __init__(self,name,gender,address):
#         self.name=name
#         self.gender=gender
#         self.address=address
        
#     def print_address(self):
#         return self.address.get_city(),self.address.pin,self.address.state
#     def edit_profile(self,new_name,new_city,new_pin,new_state):
#         self.name=new_name
#         self.address.edit_address(new_city,new_pin,new_state)
# class Address:
#     def __init__(self,city,pin,state):
#         self.__city=city
#         self.pin=pin
#         self.state=state
#     def get_city(self):
#         return self.__city
    
#     def edit_address(self,new_city,new_pin,new_state):
#         self.__city=new_city

     
# add1=Address("Muzaffarpur",843132,"Bihar")        
# cus=Customer("ritesh","male",add1)    

# print(cus.print_address())


# Inheritation

# triangle
# parents
class user:
    def __init__(self):
        self.name="ritesh"
    def login(self):
        print("login")
# child
class Student(user):
    # def __init__(self):
    #     self.rollno=100
    def enroll(self):
        print("enroll into the course")     
u=user()
s=Student()
# print(s.name)
s.login()
s.enroll()


class Phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("buying a phone")
class SearchPhone(Phone):
    # def __init__(self,os,ram):
    #     self.os=os     
    #     self.ram=ram
        print("Inside Smartphone constructor")
s=SearchPhone(2333,"Android",2)
s.brand      


