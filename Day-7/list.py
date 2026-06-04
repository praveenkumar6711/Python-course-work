Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#LIST

l=[]
type(l)
<class 'list'>
'''
A list in Python is an ordered, mutable (changeable) collection of elements enclosed in square brackets []. It can store multiple items of different data types in a single variable
'''
'\nA list in Python is an ordered, mutable (changeable) collection of elements enclosed in square brackets []. It can store multiple items of different data types in a single variable\n'
l=[1,2,3,4,5]
n=[6,7,8,9]
l+n
[1, 2, 3, 4, 5, 6, 7, 8, 9]
a*n
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a*n
NameError: name 'a' is not defined
l*5
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
l=[10,20,30,40,50]
l[4]
50
l[2]
30
l[0]
10
l[4]
50
l[-1]
50
l[-5]
10
l[+1]
20
l[-3]
30
l[:1]
[10]
l[1:]
[20, 30, 40, 50]
l[:-1]
[10, 20, 30, 40]
l[1:]
[20, 30, 40, 50]
l[1:3]
[20, 30]
l[0:5]
[10, 20, 30, 40, 50]
l[0:]
[10, 20, 30, 40, 50]
l[-1:-4:-1]
[50, 40, 30]
l[::1]
[10, 20, 30, 40, 50]
l[-3::-1]
[30, 20, 10]
l
[10, 20, 30, 40, 50]
20 in l
True
80 in l
False
40 in not in l
SyntaxError: invalid syntax
40 notin l
SyntaxError: invalid syntax
70 not in l
True
40 in l
True
l
[10, 20, 30, 40, 50]
id(1)
140719435555752
l[1]
20
l[1]
20
l[l]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    l[l]
TypeError: list indices must be integers or slices, not list
l
[10, 20, 30, 40, 50]
id(l)
2171220181184
l[4]
50
l
[10, 20, 30, 40, 50]
l.append(70)
l
[10, 20, 30, 40, 50, 70]
l.insert(1,5)
l
[10, 5, 20, 30, 40, 50, 70]
l.insert(5,60)
l
[10, 5, 20, 30, 40, 60, 50, 70]
l.del(1)
SyntaxError: invalid syntax
l.remove[1]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    l.remove[1]
TypeError: 'builtin_function_or_method' object is not subscriptable
l.remove(1)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    l.remove(1)
ValueError: list.remove(x): x not in list
l.remove(5)
l
[10, 20, 30, 40, 60, 50, 70]
l.swap(5,4)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    l.swap(5,4)
AttributeError: 'list' object has no attribute 'swap'
l.extend(80,90)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    l.extend(80,90)
TypeError: list.extend() takes exactly one argument (2 given)
l
[10, 20, 30, 40, 60, 50, 70]
l.extend([80,90])
l
[10, 20, 30, 40, 60, 50, 70, 80, 90]
l.pop(60)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    l.pop(60)
IndexError: pop index out of range
l.pop()
90
l
[10, 20, 30, 40, 60, 50, 70, 80]
l.pop(4)
60
l
[10, 20, 30, 40, 50, 70, 80]
l.push()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    l.push()
AttributeError: 'list' object has no attribute 'push'
l.remove(80)
l
[10, 20, 30, 40, 50, 70]
del l[4]
l
[10, 20, 30, 40, 70]
l.clear()
l
[]
id(l)
2171220181184
l=[100,200,3000,4000,700,554]
l
[100, 200, 3000, 4000, 700, 554]
sorted(l)
[100, 200, 554, 700, 3000, 4000]
l
[100, 200, 3000, 4000, 700, 554]
l.sort()
l
[100, 200, 554, 700, 3000, 4000]
min(1)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    min(1)
TypeError: 'int' object is not iterable
min(l)
100
max(l)
4000
l.sorted()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    l.sorted()
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> l
[100, 200, 554, 700, 3000, 4000]
>>> l.sort()
>>> l
[100, 200, 554, 700, 3000, 4000]
>>> min(l)
100
>>> max(l)
4000
>>> l.reverse()
>>> l
[4000, 3000, 700, 554, 200, 100]
>>> sorted(l.reverse=True)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> sorted(l,reverse=True)
[4000, 3000, 700, 554, 200, 100]
>>> l.index(100)
5
>>> l.index(3000)
1
>>> l.index(32)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    l.index(32)
ValueError: 32 is not in list
>>> l.count(100)
1
>>> l.count(900)
0
>>> l
[4000, 3000, 700, 554, 200, 100]
>>> len(l)
6
>>> sum(l)
8554
>>> # 0 0.0 '' () [] set() ---> FALSE
>>> any([1,2,3,4,5,6,7,8,0,0,0])
True
>>> all([1,2,3,4,5,6,0,0,0,0,0,0,,0])
SyntaxError: invalid syntax
>>> all([1,2,3,4,5,6,0,0,0,0,0,0,0])
False
