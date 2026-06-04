Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=(1,1,1,1,1,1)
t
(1, 1, 1, 1, 1, 1)
t=(1,1,1,'fdwvw',[])
t
(1, 1, 1, 'fdwvw', [])
# operations
# concatination , slicing, indexing,
t=
SyntaxError: invalid syntax
t
(1, 1, 1, 'fdwvw', [])
t=(10,20,30,40,50)
h=(90,80,70)
t+h
(10, 20, 30, 40, 50, 90, 80, 70)
t*4
(10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
t
(10, 20, 30, 40, 50)
t[1]
20
t[4]
50
t[2]
30
t[1]
20
t[-2]
40
t[-3]
30
t[-1]
50
t[:3]
(10, 20, 30)
t
(10, 20, 30, 40, 50)
t[:-3]
(10, 20)
t[-3:]
(30, 40, 50)
t[1:4]
(20, 30, 40)
t[2:]
(30, 40, 50)
t[::2]
(10, 30, 50)
t[::-1]
(50, 40, 30, 20, 10)
t[-1:-4]
()
t[-1:-4:-1]
(50, 40, 30)
t
(10, 20, 30, 40, 50)
10 in t
True
30 in t
True
60 inot in t
SyntaxError: invalid syntax
30 not in t
False
40 not in t
False
t
(10, 20, 30, 40, 50)
sorted(t)
[10, 20, 30, 40, 50]
min(t)
10
max(t)
50
t.count()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    t.count()
TypeError: tuple.count() takes exactly one argument (0 given)
t.count(t)
0
t.count(10)
1
t.count(40)
1
t.index(10)
0
a=(1,2,3)
a
(1, 2, 3)
x,y,z=a
x
1
y
2
z
3
t=(1,2,3,[4,5,6],7,8)
t
(1, 2, 3, [4, 5, 6], 7, 8)
t[2]
3
t[3]
[4, 5, 6]
>>> t[]
SyntaxError: invalid syntax
>>> t([])
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    t([])
TypeError: 'tuple' object is not callable
>>> t[3]
[4, 5, 6]
>>> t[2]=4
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
>>> t[3]
[4, 5, 6]
>>> t[3].append(10)
>>> t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
>>> s={1,2,3,4}
>>> s
{1, 2, 3, 4}
>>> s={1,1,1,1,1,1,1,1)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> s={1,1,1,1,1,1,1,1}
>>> s
{1}
>>> s={4578,48545,5654785,45,5454}
>>> s
{5654785, 4578, 48545, 45, 5454}
>>> s.add{"45,78"}
SyntaxError: invalid syntax
>>> s.add(45,78)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s.add(45,78)
TypeError: set.add() takes exactly one argument (2 given)
>>> s
{5654785, 4578, 48545, 45, 5454}
>>> s=set()
>>> s
set()
>>> s.add(1)
>>> s
{1}
