'''

#SCOPE THE FUNCTION

# local scope


def display():
    n=10
    print("Inside",n)

display()


#Global access:

n=10
def display():
    print("Inside",n)

display()
print("Outside",n)



#Modifying Global Variables:


def display():
    global n
    n=10
    print("Inside",n)

display()

print("Outside",n)



x = 10

def change():
    global x
    x = 30

change()
print(x)



def display():
    global n
    n+=10
    print("Inside",n)

n=10
display()
print("Outside",n)


#lOCAL
def outer():
    n=10
    def inner(n):
        n+=10
        print("Inner function:",n)
    inner(n)

    print("Outer function:",n)

outer()


Inner function: 20
Outer function: 10



#NON LOCAL

def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Inner function:",n)
    inner()

    print("Outer function:",n)

outer()

Inner function: 20
Outer function: 20



s='python'
print(len(s))

len=5
print(len(s))

TypeError: 'int' object is not callable



s='python'
print(len(s))

6


list,float,complex,str,list, tuple,setdef


def update(n):
    n.append(40)
    print("Inside:", n)

n = (10, 20, 30)

print("outer function:", n)

'''





