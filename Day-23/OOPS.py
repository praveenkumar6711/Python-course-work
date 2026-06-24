
#OOPS

# creating a class and object


class flipkart:
    discount =10
    products=['laptop','mouse','phone','charger']
    
#class method
    @classmethod
    def showproducts(cls):
        print(cls.products)

    def login(self,username,password):
        self.username = username
        self.password = password
        print(f"Welcome to the flipkart {self.username}")

    @staticmethod
    def banner():
        print(" 10% Discount is going on flipkart, shop now!")
        
praveen=flipkart()
praveen.login('praveen','praveenkumar@123')
praveen.banner()
praveen.showproducts()
flipkart.banner()

'''
output:
Welcome to the flipkart praveen
 10% Discount is going on flipkart, shop now!
['laptop', 'mouse', 'phone', 'charger']
 10% Discount is going on flipkart, shop now!
 '''

'''
# Attribute:
An attribute is a variable that belongs to a class or an object. It stores data or properties of an object.
Types of Attributes:

Instance Attributes – Specific to each object.
Class Attributes – Shared by all objects of a class.


# Types of Methods in Python
1. Instance Method:
Works with object data (instance attributes).

2. Class Method
Works with class attributes.

3. Static Method
Does not use object data or class data.
'''
