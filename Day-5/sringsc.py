Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# STRINGS
a='python'
b='codegnan'
a+b
'pythoncodegnan'
a-b
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a-b
TypeError: unsupported operand type(s) for -: 'str' and 'str'
s='python programming"
SyntaxError: unterminated string literal (detected at line 1)
s='python programming'
s
'python programming'
s=''
s
''
a='codegnan'
b='pfs'
a+b
'codegnanpfs'
type(a)
<class 'str'>
a*10
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
'*'*20
'********************'
'python'*5
'pythonpythonpythonpythonpython'
'python '*8
'python python python python python python python python '


#indexing

names = "praveen ram sita ramu vamsi"
names
'praveen ram sita ramu vamsi'
>>> names[4]
'e'
>>> names[2]
'a'
>>> names[12]
's'
>>> names[19]
'm'
>>> names[-1]
'i'
>>> names[-3]
'm'
>>> names
'praveen ram sita ramu vamsi'
>>> names[:6]
'pravee'
>>> names[:7]
'praveen'
>>> names[7:10]
' ra'
>>> names[7:11]
' ram'
>>> names[11:16]
' sita'
>>> names[16:21]
' ramu'
>>> names[21:27]
' vamsi'
>>> names[21:28]
' vamsi'
>>> names[-1:-6]
''
>>> names[:-7]
'praveen ram sita ram'
>>> names[-7:]
'u vamsi'
>>> names[-6]
' '
>>> names[-6:]
' vamsi'
>>> names[-6:-11]
''
>>> names[-6::-12]
' a'
>>> names[::-1]
'ismav umar atis mar neevarp'
