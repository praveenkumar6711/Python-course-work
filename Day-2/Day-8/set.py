Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets
s={1,2,3,4,5}
s
{1, 2, 3, 4, 5}
s={784545,545745,545545,2531564,87}
s
{784545, 545745, 87, 545545, 2531564}
s=set(1)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s=set(1)
TypeError: 'int' object is not iterable
s=set()
s
set()
s.add(1)
s
{1}
s.add(45,68)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s.add(45,68)
TypeError: set.add() takes exactly one argument (2 given)
s.add(45.68)
s
{1, 45.68}
s.add("dasgsfdgwr")
s
{1, 'dasgsfdgwr', 45.68}
s.add((1:1,2:2))
SyntaxError: invalid syntax
s
{1, 'dasgsfdgwr', 45.68}
1 in s
True
2 in s
False
False not in s
True

#operations
a={1,2,3,4,5,6,7,10}
b={6,7,8,9}
a|b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a.intersection(b)
{6, 7}
a&b
{6, 7}
a - b
{1, 2, 3, 4, 5, 10}
a ^ b
{1, 2, 3, 4, 5, 8, 9, 10}
a + b
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a + b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a*b
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a*b
TypeError: unsupported operand type(s) for *: 'set' and 'set'
a-b
{1, 2, 3, 4, 5, 10}
a ^ b
{1, 2, 3, 4, 5, 8, 9, 10}

# subset annd superset
a
{1, 2, 3, 4, 5, 6, 7, 10}
#{1}{2}{3}{5}{1,3}{1,2}{1,3}{8,10}
a<={1}
False
a<={1,2,3,4,5,6,7,8,9}
False
a<={1,2,3,4,5,6,7,8,9,9}
False
a>={6,7,8,9}
False
a<= {1,2,3,4,5,6,8,10,11,12}
False
a>={6,10,8}
False
a
{1, 2, 3, 4, 5, 6, 7, 10}
b
{8, 9, 6, 7}
a.isdisjoint(b)
False
a
{1, 2, 3, 4, 5, 6, 7, 10}
a.add(17)
a
{1, 2, 3, 4, 5, 6, 7, 10, 17}
a.pop()
1
a.pop()
2
a.remove(10)
a
{3, 4, 5, 6, 7, 17}
a.discard(3)
a
{4, 5, 6, 7, 17}
a.discard(3)
a
{4, 5, 6, 7, 17}
>>> a
{4, 5, 6, 7, 17}
>>> a.clear()
>>> a
set()
>>> a={1,23,4,57,235}
>>> b={1,2,34,4}
>>> a
{1, 4, 23, 57, 235}
>>> b
{1, 2, 4, 34}
>>> a.intersection_update(b)
>>> a
{1, 4}
>>> b
{1, 2, 4, 34}
>>> c=b
>>> c.add(12)
>>> c
{1, 2, 34, 4, 12}
>>> c
{1, 2, 34, 4, 12}
>>> b
{1, 2, 34, 4, 12}
>>> d = c.copy()
>>> d.add(10)
>>> a
{1, 4}
>>> b
{1, 2, 34, 4, 12}
>>> c
{1, 2, 34, 4, 12}
>>> len(c)
5
>>> min(c)
1
>>> max(c)
34
>>> sorted(c)
[1, 2, 4, 12, 34]
>>> sum(c)
53
>>> c.add(12)
>>> c
{1, 2, 34, 4, 12}
