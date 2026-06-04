Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s="     hello     world    "
s
'     hello     world    '
s.strip()
'hello     world'
s.lstrip()
'hello     world    '
s.rstrip()
'     hello     world'
s
'     hello     world    '
s.startwith()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.startwith()
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
s.startwith.py
Traceback (most recent call last):

  File "<pyshell#7>", line 1, in <module>
    s.startwith.py
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
s.startwith('str')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s.startwith('str')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
s.startswith('str')
False
s='string.py'
s
'string.py'
s.startswith()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.startswith()
TypeError: startswith expected at least 1 argument, got 0
s.startswith('str')
True
s.startswith("py")
False
>>> KeyboardInterrupt
>>> s.endswith("py")
True
>>> s.endswith("js")
False
>>> s.startswith("sdhj")
False
>>> 'dksfksdjghoer'.isalpha()
True
>>> '3241'.isalpha()
False
>>> "abc123".isalnum()
True
>>> "egjfkshdfjghir".isalnum()
True
>>> "@#$".isalnum()
False
>>> "hello".islower()
True
>>> "Hello".isupper()
False
>>> "HELLO".isupper()
True
>>> " ".is space()
SyntaxError: invalid syntax
>>> " ".isspace()
True
>>> "".isspace()
False
>>> "sdnkjfheajkhdfunerkjfhi".islower()
True
>>> "helloo            ".isspace()
False
>>> "py dnsnkfhidu kjrfgj".istitle()
False
>>> "Pjfedhguj Aeffnui Djkerjgijeri".istitle()
True
>>> "hello".isidentifier()
True
>>> "1hello".isidentifier()
False
>>> "hello121456".isidentifier()
True
>>> " ".isidentifier()
False
