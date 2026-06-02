Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python programming'
len(s)
18
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
min(s)
' '
max(s)
'y'
ord(s)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ord(s)
TypeError: ord() expected a character, but string of length 18 found
ord('a')
97
ord('b')
98
ord('A')
65
ord('1')
49
KeyboardInterrupt
ord('0')
48
ord(' ')
32
chr(120)
'x'
chr(30)
'\x1e'
chr(35)
'#'
chr(37)
'%'
chr(65)
'A'
s='python programming'
s.upper()
'PYTHON PROGRAMMING'
s.lower()
'python programming'
s.tittle()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s.tittle()
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
s.title()
'Python Programming'
s.swapcase()
'PYTHON PROGRAMMING'
s
'python programming'
s.center(38,'*')
'**********python programming**********'
s.center(26,'--')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.center(26,'--')
TypeError: The fill character must be exactly one character long
s.center(26,'-')
'----python programming----'
s.center(28,'-')
'-----python programming-----'
"123".zfill(5)
'00123'

"123".zfill(10)
'0000000123'
"123".zfill(3)
'123'
s
'python programming'
s.find('4')
-1
s.find('o')
4
s.find('g')
10
s.find('o')
4
s.rfind('0')
-1
s.rfind('o')
9
s.rindex('o')
9
s
'python programming'
s.count('y')
1
s.count('g')
2
s.count('m')
2
s.count('p')
2
s.replace('python','java')
'java programming'
s.maketrans(('python','1234566')
            )
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s.maketrans(('python','1234566')
TypeError: if you give only one argument to maketrans it must be a dict
s.maketrans(('python','123456'))
                
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s.maketrans(('python','123456'))
TypeError: if you give only one argument to maketrans it must be a dict
s.maketrans('python','1234566')
                
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    s.maketrans('python','1234566')
ValueError: the first two maketrans arguments must have equal length
s.maketrans('python','123456')
                
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
s.translate(s.maketrans('python','123456')
            )
                
'123456 1r5grammi6g'
s='java,python,javascript,c,c++')
    
SyntaxError: unmatched ')'
s='java,python,javascript,c,c++'
s.split(',')
['java', 'python', 'javascript', 'c', 'c++']
s.split(',',2)
['java', 'python', 'javascript,c,c++']
g='ssdfjnek'
g'''feafcerae
erfveawvfer
'''
SyntaxError: invalid syntax
g=
'''feafcerae
... erfveawvfer
... '''
SyntaxError: invalid syntax
>>> g
'ssdfjnek'
>>> g='''asjknfjksdabhejfenjk'''
>>> g='''knefjbgjkwerb
... sdfnhgnej
... '''
>>> g
'knefjbgjkwerb\nsdfnhgnej\n'
>>> s.splitlines()
['java,python,javascript,c,c++']
>>> 
>>> g.splitlines()
['knefjbgjkwerb', 'sdfnhgnej']
>>> l=['java','python','javascript','c']
>>> ''.join(l)
'javapythonjavascriptc'
>>> '-'.join(l)
'java-python-javascript-c'
>>> ' '.join(l)
'java python javascript c'
>>> ','.join(l)
'java,python,javascript,c'
>>> '@'.join(l)
'java@python@javascript@c'
>>> # partition
>>> s
'java,python,javascript,c,c++'
>>> s.partition(',')
('java', ',', 'python,javascript,c,c++')
>>> s.rpartition(',')
('java,python,javascript,c', ',', 'c++')
>>> t="Hello 😀"
>>> t.encode()
b'Hello \xf0\x9f\x98\x80'
>>> b'Hello \xf0\x9f\x98\x80'.decode()
'Hello 😀'
