'''

WHILE LOOPS
i = 1

while i <= 5:
    print(i)
    i += 1



i = 2

while i <= 21:
    print(i)
    i += 2


i = 10

while i > 0:
    print(i)
    i -= 1

i = 5

while i < 51:
    print(i)
    i += 5

l=[2,436,5467,7657,55,7,6]
i=0
while i<len(l):
    print(l[i])
    i+=1
    
l=(2,436,5467,7657,55,7,6)
i=0
while i<len(l):
    print(l[i])
    i+=1


l = [1,1,1,1,1,2,3,435,3,55,53,2,2,2,2,4,4,4,45,5,5,5,5,0,0,0,0,0,0,12,123]

i = 0

while i < len(l):
    if l[i] == 0:
        l.pop(i)
    else:
        i += 1

print(l)
'''


