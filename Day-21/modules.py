
'''
import sys

print(sys.argv)
print(sys.path)
print(sys.version)

print("Before exit")
sys.exit()
print("After exit")


['C:/Users/prave/OneDrive/Desktop/Python-course-work/Day-21/modules.py']
['C:/Users/prave/OneDrive/Desktop/Python-course-work/Day-21', 'C:\\Program Files\\Python313\\Lib\\idlelib', 'C:\\Program Files\\Python313\\python313.zip', 'C:\\Program Files\\Python313\\DLLs', 'C:\\Program Files\\Python313\\Lib', 'C:\\Program Files\\Python313', 'C:\\Users\\prave\\AppData\\Roaming\\Python\\Python313\\site-packages', 'C:\\Users\\prave\\AppData\\Roaming\\Python\\Python313\\site-packages\\win32', 'C:\\Users\\prave\\AppData\\Roaming\\Python\\Python313\\site-packages\\win32\\lib', 'C:\\Users\\prave\\AppData\\Roaming\\Python\\Python313\\site-packages\\Pythonwin', 'C:\\Program Files\\Python313\\Lib\\site-packages']
3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)]
Before exit
'''

'''

import platform

print(platform.system(),platform.release(),platform.processor())

Windows 11 Intel64 Family 6 Model 154 Stepping 4, GenuineIntel


'''

'''
import math

print(math.pi)
print(math.e)

print(math.sqrt(25))
print(math.pow(2,5))

print(math.ceil(12.3))
print(math.ceil(12.0000001))
print(math.ceil(12.99999999))
print(math.ceil(12.8))

print(math.floor(12.3))
print(math.floor(12.000001))
print(math.floor(12.9999999))
print(math.floor(12.8))


3.141592653589793
2.718281828459045
5.0
32.0
13
13
13
13
12
12
12
12


'''

'''
import math

print(math.fabs(-12))
print(math.factorial(5))
print(math.gcd(0,20))


print(math.log(10,10))
print(math.sin(10))
print(math.cos(10))
print(math.tan(10))

print(math.degrees(20))
print(math.radians(20))


12.0
120
20
1.0
-0.5440211108893698
-0.8390715290764524
0.6483608274590866
1145.9155902616465
0.3490658503988659


'''

'''
#random module

import random

print(random.random())
print(random.randint(1, 10))
print(random.uniform(1, 10))

l = ['python', 'c', 'c++', 'java', 'html']

print(random.choice(l))
print(random.choices(l, k=3))

s = 'rps'
print(random.choice(s))

print(l)
random.shuffle(l)
print(l)

0.12738404920552293
10
9.71518284486486
java

['c++', 'java', 'c']
s
['python', 'c', 'c++', 'java', 'html']
['java', 'python', 'c', 'html', 'c++']


      '''
'''
import collections

s = 'python programming language'

print(collections.Counter(s))

d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

Counter({'g': 4, 'n': 3, 'a': 3, 'p': 2, 'o': 2, ' ': 2, 'r': 2, 'm': 2, 'y': 1, 't': 1, 'h': 1, 'i': 1, 'l': 1, 'u': 1, 'e': 1})
{'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 3, ' ': 2, 'r': 2, 'g': 4, 'a': 3, 'm': 2, 'i': 1, 'l': 1, 'u': 1, 'e': 1}
'''


'''
import collections

s = 'python programming language'

d=collections.defaultdict(int)

for i in s:
    d[i] += 1

print(d)

defaultdict(<class 'int'>, {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 3, ' ': 2, 'r': 2, 'g': 4, 'a': 3, 'm': 2, 'i': 1, 'l': 1, 'u': 1, 'e': 1})


'''
'''
import collections

l = collections.deque()

l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)

print(l)

l.pop()
l.pop()
l.pop()

print(l)

l.appendleft(50)
l.appendleft(60)

print(l)

l.pop()

print(l)

deque([40, 30, 20, 10])
deque([40])
deque([60, 50, 40])
deque([60, 50])

'''

'''
import itertools

print(list(itertools.combinations("abcd",2)))
print(list(itertools.permutations("abcd",2)))


[('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]
[('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'a'), ('b', 'c'), ('b', 'd'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('d', 'a'), ('d', 'b'), ('d', 'c')]
'''


from itertools import combinations,permutations

com=combinations('abcd',2)
print([''.join(i) for i in com])

per=permutations('abcd',2)
print([''.join(i) for i in per])

['ab', 'ac', 'ad', 'bc', 'bd', 'cd']
['ab', 'ac', 'ad', 'ba', 'bc', 'bd', 'ca', 'cb', 'cd', 'da', 'db', 'dc']
