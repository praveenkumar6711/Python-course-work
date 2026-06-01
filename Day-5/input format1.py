Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
b=20
print(a<b)
True
print(a>b)
False
'''
input formating
'''
'\ninput formating\n'
name=input()
praveen
name
'praveen'
name=input("enter your name:")
enter your name:praveen
name
'praveen'
age=input("enter your age:")
enter your age:25
age
'25'
age=int(input()
        age=12
        
SyntaxError: '(' was never closed
age=int(input("enter your age:"))
        
enter your age:21
type(age)
        
<class 'int'>
gpa=float(input("enter your gpa:")
          8.9
          
SyntaxError: '(' was never closed
gpa=float(input("enter your gpa:"))
          
enter your gpa:8.9
type(age)
          
<class 'int'>
type(gpa)
          
<class 'float'>
'praveen ramu ram suresh'
          
'praveen ramu ram suresh'
'praveen ramu ram suresh'.split('')
          
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    'praveen ramu ram suresh'.split('')
ValueError: empty separator
'praveen ramu ram suresh'.split(' ')
          
['praveen', 'ramu', 'ram', 'suresh']
#
          
int - int(input())
          
float - float(input())
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int - int(input())
ValueError: invalid literal for int() with base 10: 'float - float(input())'
'java-python-sql,html'
          
'java-python-sql,html'
names= input("enter the names: ").split()
          
enter the names: praveen ramu ram suresh
names
          
['praveen', 'ramu', 'ram', 'suresh']
products =input("enter the products: ").split()
          
enter the products: laptop mouse cpu charger keyboard
products
          
['laptop', 'mouse', 'cpu', 'charger', 'keyboard']
topics=tuple(input("enter the topics:").split())
          
enter the topics:token statement variable comments
topics
          
('token', 'statement', 'variable', 'comments')
op=set(input("enter the operators:").split())
          
enter the operators:in not is is not and or not
op
          
{'or', 'not', 'and', 'in', 'is'}
marks=input("enter the marks:").split
          
enter the marks:45 56 74 12 23
marks
          
<built-in method split of str object at 0x0000025026D74F30>
marks=input("enter the marks:").split()
          
enter the marks:45 56 74 12 23
marks
          
['45', '56', '74', '12', '23']
# map function
          
map (int,input("enter the marks":).split()
     
SyntaxError: invalid syntax
map (int,input("enter the marks:").split()
     )
     
enter the marks:5 6 7 8 9 7
<map object at 0x0000025026DE1000>
# list
     
list(map(int,input("enter the marks:").split())
     )
     
enter the marks:5 4 7 9 6 3
[5, 4, 7, 9, 6, 3]
prices=tuple(map(int,input("enter the prices:").split())
             )
     
enter the prices:4578 3658 45896 33356
prices
     
(4578, 3658, 45896, 33356)
rating=set(map(int,input("enter the rating:").split())
           )
     
enter the rating:4 5 9 7 3.4
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    rating=set(map(int,input("enter the rating:").split())
ValueError: invalid literal for int() with base 10: '3.4'
rating=set(map(int,input("enter the rating:").split())
           )
               
enter the rating:5 6 8 7 1 3 9 4
rating
               
{1, 3, 4, 5, 6, 7, 8, 9}
rating=set(map(float,input("enter the rating:").split()))
               
enter the rating:4.5 1.5 3.6 8.4
rating
               
{8.4, 1.5, 3.6, 4.5}
rating=set(map(int,float,input("enter the rating:").split()))
               
enter the rating:4.2 4 6.7
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    rating=set(map(int,float,input("enter the rating:").split()))
TypeError: 'type' object is not iterable
type(rating)
               
<class 'set'>
rating=set(map(int,input("enter the rating:").split())
           )

             
enter the rating:4 5 6 8 9 99 77
rating
               
{99, 4, 5, 6, 8, 9, 77}
percentage=list(map,input("enter the percentage:").split()))
     
SyntaxError: unmatched ')'
percentage=list(map,input("enter the percentage:").split())
     
enter the percentage:45.2 45.6   55.3 89.6
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    percentage=list(map,input("enter the percentage:").split())
TypeError: list expected at most 1 argument, got 2
percentage=list(map,input("enter the percentage:").split())
     
enter the percentage:12.2 4.5 13.2
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    percentage=list(map,input("enter the percentage:").split())
TypeError: list expected at most 1 argument, got 2
percentage=list(map(float,input("enter the percentage:").split()))
     
enter the percentage:4.5 2.3 6.4
percentage
     
[4.5, 2.3, 6.4]
prices=set(map(float,input("enter the prices:").split()))
     
enter the prices:1.2 35.6 45.1
prices
     
{1.2, 35.6, 45.1}
a,b=10,20
     
a
     
10
b
     
20
a,b=[10,20]
     
a
     
10
b
     
20
username,password=input("enter the username & password:").split())
          
SyntaxError: unmatched ')'
username,password=input("enter the username & password:").split()
          
enter the username & password:codegnan
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    username,password=input("enter the username & password:").split()
ValueError: not enough values to unpack (expected 2, got 1)
username,password=input("enter the username,password:").split()
          
enter the username,password:codegnan
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    username,password=input("enter the username,password:").split()
ValueError: not enough values to unpack (expected 2, got 1)
username,password=input("enter the username & password:").split()
          
enter the username & password:praveen 4556566
username
          
'praveen'
password
          
'4556566'
a,b,c,d=list(map(int,input("enter the 4 slides:").split()))
          
enter the 4 slides:6 4 3 9
a
          
6
b
          
4
c
          
3
d
          
9
a+b
          
10
d-a
          
3
a/b
          
1.5
a*d
          
54
price,discount=list(map(float,input().split()))
          
)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    price,discount=list(map(float,input().split()))
ValueError: could not convert string to float: ')'
price,discount = list(map(float,input().split()))
        
price,discount = list(map(float,input().split())))
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    price,discount = list(map(float,input().split()))
ValueError: could not convert string to float: 'price,discount'
price,discount=list(map(float,input().split()))
price
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    price,discount=list(map(float,input().split()))
ValueError: could not convert string to float: 'price'
price,discount=list(map(float,input().split()))
12
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    price,discount=list(map(float,input().split()))
ValueError: not enough values to unpack (expected 2, got 1)
price,discount=list(map(float,input().split()))
456 15.4
price
456.0
discount
15.4
a=eval(input())
455465.1
a
455465.1
a=eval(input())
'pyhton'
a
'pyhton'
a=eval(input())
[1,2,3,4,5,6]
a
[1, 2, 3, 4, 5, 6]
type(a)
<class 'list'>
a=eval(input())
(34,56,78)
a
(34, 56, 78)
type(a)
<class 'tuple'>
a=eval(input())
{23,45,67}
a
{67, 45, 23}
type(a)
<class 'set'>
a=eval(input())
['a''b''c'}
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1
    ['a''b''c'}
              ^
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a=eval(input())
['14''45'}
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1
    ['14''45'}
             ^
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a=eval(input())
('1''56')
>>> a=
SyntaxError: invalid syntax
>>> a
'156'
>>> type(a)
<class 'str'>
>>> ['14''45'}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a=eval(input())
[3:4,4:8]
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1
    [3:4,4:8]
      ^
SyntaxError: invalid syntax
>>> a=eval(input())
{4:5,2:3}
>>> a
{4: 5, 2: 3}
>>> type(a)
<class 'dict'>
>>> a=eval(input())
True
>>> a
True
>>> type(a)
<class 'bool'>
>>> 
>>> 
>>> '''
... STRINGS
... collection of items
... string is an immmutable datatype - cannot change
... '''
'\nSTRINGS\ncollection of items\nstring is an immmutable datatype - cannot change\n'
