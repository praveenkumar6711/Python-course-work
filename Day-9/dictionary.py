Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#DICTIONARY

#IS IS A COLLECTION OF KEY PAIR VALUES AND ITS  IS AN ORDERED AND ITS IMMUTABLE

d=()
d=dict()
type(d)
<class 'dict'>
d[1]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    d[1]
KeyError: 1
d={'k1':'k2'}
d
{'k1': 'k2'}
d=()
d
()
d{1]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
d{}
SyntaxError: invalid syntax
d={}
d
{}
d={'k1':'k2':'k3'}
SyntaxError: invalid syntax
d={'k1':'k2','k3':'v2'}
d
{'k1': 'k2', 'k3': 'v2'}
d[1]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    d[1]
KeyError: 1
d{1}
SyntaxError: invalid syntax
d={}
d{1}
SyntaxError: invalid syntax
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d['demo']='str'
d
{1: 'int', 12.3: 'float', 'demo': 'str'}
d[2+3j]='complex'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
d[False]='bool'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex', False: 'bool'}
d={}
d
{}
d(1)=1
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
d'
SyntaxError: unterminated string literal (detected at line 1)
d
{}
d[2+3j]='complex'
d
{(2+3j): 'complex'}
d[False]='bool'
d
{(2+3j): 'complex', False: 'bool'}
d={}
d[1]=1
d
{1: 1}
d[23]=23.4
d
{1: 1, 23: 23.4}
d[31]='sdvfd'
d[4]=3+4j
d[5]=[1,2,3,4]
d[6]=(1,2,3)
d[7]=(1,3)
d[8]={1:1,2:2}
d[9]=False
d
{1: 1, 23: 23.4, 31: 'sdvfd', 4: (3+4j), 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: (1, 3), 8: {1: 1, 2: 2}, 9: False}
d[1]=14
d
{1: 14, 23: 23.4, 31: 'sdvfd', 4: (3+4j), 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: (1, 3), 8: {1: 1, 2: 2}, 9: False}
d={}
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d[3]
2
d={1:2,2:4,3:6,4:8,5:10,6:12}
d[4]
8
d[6]
12
d[1]
2
d[4]
8
d={'praveen':78,'pradeep':95,'subbu':85,'vivek':76}
d['pradeep']
95
d['subbu']
85
d['praveen']
78
d['vivek']
76
d.get('venky')
d.get('nani')
d
{'praveen': 78, 'pradeep': 95, 'subbu': 85, 'vivek': 76}
d.get('akhil','user not found')
'user not found'
d.get('subbu',user not found')
      
SyntaxError: unterminated string literal (detected at line 1)
d.get('subbu','user not found')
      
85
d
      
{'praveen': 78, 'pradeep': 95, 'subbu': 85, 'vivek': 76}
'vivek' in d
      
True
'srikanth' in d
      
False
d.keys()
      
dict_keys(['praveen', 'pradeep', 'subbu', 'vivek'])
d.values()
      
dict_values([78, 95, 85, 76])
d.items()
      
dict_items([('praveen', 78), ('pradeep', 95), ('subbu', 85), ('vivek', 76)])
sorted(d)
      
['pradeep', 'praveen', 'subbu', 'vivek']
max(d)
      
'vivek'
min(d)
      
'pradeep'
d
      
{'praveen': 78, 'pradeep': 95, 'subbu': 85, 'vivek': 76}
len(d)
      
4
d
      
{'praveen': 78, 'pradeep': 95, 'subbu': 85, 'vivek': 76}

#accesing methods
      
d
      
{'praveen': 78, 'pradeep': 95, 'subbu': 85, 'vivek': 76}
d['dinesh]
  
SyntaxError: unterminated string literal (detected at line 1)
d['dinesh']
  
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    d['dinesh']
KeyError: 'dinesh'
d['subbu'
  98
  
SyntaxError: '[' was never closed
d['subbu']
  
85
d['subbu']=100
  
d
  
{'praveen': 78, 'pradeep': 95, 'subbu': 100, 'vivek': 76}
d['rishi']=98
  
d
  
{'praveen': 78, 'pradeep': 95, 'subbu': 100, 'vivek': 76, 'rishi': 98}
d.update('praneeth':90,'manideeo':84)
  
SyntaxError: invalid syntax
d.update(('praneeth':90,'manideeo':84))
  
SyntaxError: invalid syntax
d.update(['praneeth':90,'manideeo':84])
  
SyntaxError: invalid syntax
d.update({'praneeth':90,'manideeo':84})
...   
>>> d
...   
{'praveen': 78, 'pradeep': 95, 'subbu': 100, 'vivek': 76, 'rishi': 98, 'praneeth': 90, 'manideeo': 84}
>>> d.popitem()
...   
('manideeo', 84)
>>> d.pop('pradeep')
...   
95
>>> d
...   
{'praveen': 78, 'subbu': 100, 'vivek': 76, 'rishi': 98, 'praneeth': 90}
>>> d.pop('rishi')
...   
98
>>> d
...   
{'praveen': 78, 'subbu': 100, 'vivek': 76, 'praneeth': 90}
>>> del d['praneeth']
...   
>>> d
...   
{'praveen': 78, 'subbu': 100, 'vivek': 76}
>>> d.clear()
...   
>>> d
...   
{}
>>> d={'praveen': 78, 'pradeep': 95, 'subbu': 100, 'vivek': 76, 'rishi': 98, 'praneeth': 90, 'manideeo': 84}
...   
>>> d
...   
{'praveen': 78, 'pradeep': 95, 'subbu': 100, 'vivek': 76, 'rishi': 98, 'praneeth': 90, 'manideeo': 84}
>>> d.setdefault('rishi',0)
...   
98
>>> d
...   
{'praveen': 78, 'pradeep': 95, 'subbu': 100, 'vivek': 76, 'rishi': 98, 'praneeth': 90, 'manideeo': 84}
>>> d.setdefault('ramu',0)
...   
0
>>> d
...   
{'praveen': 78, 'pradeep': 95, 'subbu': 100, 'vivek': 76, 'rishi': 98, 'praneeth': 90, 'manideeo': 84, 'ramu': 0}
