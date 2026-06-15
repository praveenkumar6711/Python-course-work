'''
A function is a reusable block of code that performs a specific task.
Functions are defined using the def keyword.
They help in reducing code duplication.


def function_name(args):
    #stmts
    return


function_num(para)




def wish(name):
    print(f'welcome to the python course {name}')

wish('subbu')
wish('praveen')
wish('siddhu')





def iseven(num):
    if num%2==0:
        return f"{num} - Even Number"
    else:
        return f"{num} - Odd Number"

print(iseven(12))
print(iseven(13))




def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

num = int(input("Enter the number: "))
print("Factorial:", factorial(num))



def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num}-Not Prime Number"
        return f"{num}-Prime Number"

num=int(input("Enter the number:"))
print(isprime(num))



Arguments:
    1.positional
    2.key
    3.def
    4.var

# POSITIONAL ARGUMENTS

def display(name,email,password):
    print("Name:",name)
    print("Email:",email)
    print("Password:",password)

display('praveen','praveen@gmail.com','Praveen@567')
display('Praveen@567','praveen@gmail.com','Praveen')
display('praveen@gmail.com','Praveen@567','Praveen')

Name: praveen
Email: praveen@gmail.com
Password: Praveen@567
Name: Praveen@567
Email: praveen@gmail.com
Password: Praveen
Name: praveen@gmail.com
Email: Praveen@567
Password: Praveen



#KEYWORD ARGUMENTS

def display(name,email,password):
    print("Name:",name)
    print("Email:",email)
    print("Password:",password)


display(name='praveen',email='praveen@gmail.com',password='Praveen@567')
display(password='Praveen@567',email='praveen@gmail.com',name='Praveen')
display(email='praveen@gmail.com',password='Praveen@567',name='Praveen')

Output:

Name: praveen
Email: praveen@gmail.com
Password: Praveen@567
Name: Praveen
Email: praveen@gmail.com
Password: Praveen@567
Name: Praveen
Email: praveen@gmail.com
Password: Praveen@567




#default Argument:

def display(name,email,pwd=''):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)

display('praveen','praveen@gmail.com','Praveen@567')
display('praveen@gmail.com','Praveen')


Name: praveen
Email: praveen@gmail.com
Password: Praveen@567
Name: praveen@gmail.com
Email: Praveen
Password: 




# Variable Length Argument:


def display(*names):
    print("Names:",names)

display('praveen','mani','uday','nithesh')
display('naresh','Praveen','suresh')
display('raju','Praveen')
display('ravi')

output:
    
Names: ('praveen', 'mani', 'uday', 'nithesh')
Names: ('naresh', 'Praveen', 'suresh')
Names: ('raju', 'Praveen')
Names: ('ravi',)

  '''
def display(**names):
    print("Names:",names)

display(k1='praveen',k2='mani',k3='uday',k4='nithesh')
display(k1='naresh',k2='Praveen',k3='suresh')
display(k1='raju',k2='Praveen')
display(k1='ravi')


