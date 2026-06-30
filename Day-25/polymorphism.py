
'''
#Polymorphism
Polymorphism is an OOP concept in which the same method or function behaves differently for different objects.

1. Compile-time Polymorphism (Method Overloading):
    Python does not support true method overloading directly, but it can be achieved using default arguments.

2. Run-time Polymorphism (Method Overriding):
    A child class provides its own implementation of a method already defined in the parent class.

'''

'''
#Method Overriding (Runtime Polymorphism).

    
class Hotstar:
    def __init__(self,name):
        self.name = name
        print(f"Hi {self.name}, Welcome to the hotstar")
    def login(self):
        print("You can login")
    def dashboard(self):
        print("You can  see the dashboard items")
    def search(self):
        print("You can search")
    def languages(self):
        print("You select the languages")
    def playcontrollers(self):
        print("You can login")
    def login(self):
        print("You can pause and play the vedio")
    def ads(self):
        print("Ads will run")
    def movies(self):
        print("You can limited access for movies")
    def sports(self):
        print("limited time you can watch sports")
    def quality(self):
        print("limited quality")

praveen =Hotstar('praveen')
praveen.login()
praveen.dashboard()
praveen.search()
praveen.languages()
praveen.playcontrollers()
praveen.login()
praveen.ads()
praveen.movies()
praveen.sports()
praveen.quality()


Hi praveen, Welcome to the hotstar
You can pause and play the vedio
You can  see the dashboard items
You can search
You select the languages
You can login
You can pause and play the vedio
Ads will run
You can limited access for movies
limited time you can watch sports
limited quality

   '''
'''
# Method Overriding

class Hotstar:
    def __init__(self,name):
        self.name = name
        print(f"Hi {self.name}, Welcome to the hotstar")
    def login(self):
        print("You can login")
    def dashboard(self):
        print("You can  see the dashboard items")
    def search(self):
        print("You can search")
    def languages(self):
        print("You select the languages")
    def playcontrollers(self):
        print("You can login")
    def login(self):
        print("You can pause and play the vedio")
    def ads(self):
        print("Ads will run")
    def movies(self):
        print("You can limited access for movies")
    def sports(self):
        print("limited time you can watch sports")
    def quality(self):
        print("limited quality")
        
class PremiumHotstar(Hotstar):
    def __init__(self,name):
        self.name = name
        print(f"Hi {self.name}, Welcome to the Premium hotstar")
        
    def ads(self):
        print("Ads won't run")
    def movies(self):
        print("You can unlimited access for movies")
    def sports(self):
        print("you can watch sports")
    def quality(self):
        print("High quality")

praveen =PremiumHotstar('praveen')
praveen.login()
praveen.dashboard()
praveen.search()
praveen.languages()
praveen.playcontrollers()
praveen.login()
praveen.ads()
praveen.movies()
praveen.sports()
praveen.quality()

Hi praveen, Welcome to the Premium hotstar
You can pause and play the vedio
You can  see the dashboard items
You can search
You select the languages
You can login
You can pause and play the vedio
Ads won't run
You can unlimited access for movies
you can watch sports
High quality

'''

'''
#operator Overloading:
#Operator overloading gives a new meaning to operators for user-defined objects.



class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

    def __sub__(self, other):
        return self.n - other.n

    def __mul__(self, other):
        return self.n * other.n

    def __eq__(self, other):
        return self.n == other.n

    def __lt__(self, other):
        return self.n < other.n

    def __gt__(self, other):
        return self.n > other.n

    def __truediv__(self, other):
        return self.n / other.n

    def __str__(self):
        return str(self.n)


n1 = Number(20)
n2 = Number(10)

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 == n2)
print(n1 < n2)
print(n1 > n2)
print(n1 / n2)
print(n1, n2)

    
30
10
200
False
False
True
2.0
20 10
    
'''
