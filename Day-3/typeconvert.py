Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
bool(a)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    bool(a)
NameError: name 'a' is not defined
a=10
bool(a)
True
bool(0.0)
False
c=2+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
bool(b)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    bool(b)
NameError: name 'b' is not defined
str(c)
'(2+3j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
bool(c)
True
dict(c)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
s="python"
a='1,2,3,4,5'
b='324324.432'
int(s)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'python'
int(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: '1,2,3,4,5'
a='12142134'
int(a)
12142134
int(b)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: '324324.432'
float(b)
324324.432
list(s)
['p', 'y', 't', 'h', 'o', 'n']
list(b)
['3', '2', '4', '3', '2', '4', '.', '4', '3', '2']
tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
set("s)
    
SyntaxError: unterminated string literal (detected at line 1)
set(s)
    
{'h', 'y', 'o', 't', 'p', 'n'}
dict(s)
    
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
    
True
complex(s)
    
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
complex(a)
    
(12142134+0j)
complex(b)
    
(324324.432+0j)
l=[1,2,3,4,5]
    
l
    
[1, 2, 3, 4, 5]
int(l)
    
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
    
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
    
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
str(l)
    
'[1, 2, 3, 4, 5]'
list*l)
SyntaxError: unmatched ')'
list(l)
[1, 2, 3, 4, 5]
tuple(l)
(1, 2, 3, 4, 5)
set(l)
{1, 2, 3, 4, 5}
dict(l)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
type(l)
<class 'list'>
s=(12,34,56)
int(s)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
str(s)
'(12, 34, 56)'
float(s)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'tuple'
list(a)
['1', '2', '1', '4', '2', '1', '3', '4']
list(s)
[12, 34, 56]
>>> tuple(s)
(12, 34, 56)
>>> set(s)
{56, 34, 12}
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(s)
True
>>> type(s)
<class 'tuple'>
>>> s = {1, 2, 3, 4}
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
>>> list(s)
[1, 2, 3, 4]
>>> tuple(s)
(1, 2, 3, 4)
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(s)
True
>>> type(s)
<class 'set'>
