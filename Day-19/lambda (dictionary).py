
'''
d={'sugar':40,'salt':20,'cooking oil':80,'chilli':60}

res=dict(map(lambda i: (i[0],i[1]+i[1]*0.18),d.items()))
res1=dict(map(lambda i: (i[0],i[1]-i[1]*0.5),d.items()))

print(res)
print(res1)

{'sugar': 47.2, 'salt': 23.6, 'cooking oil': 94.4, 'chilli': 70.8}
{'sugar': 20.0, 'salt': 10.0, 'cooking oil': 40.0, 'chilli': 30.0}




#Filter

d={'sugar':40,'salt':20,'cooking oil':80,'chilli':60}

res=dict(filter(lambda i: i[1]>50,d.items()))
res1=dict(filter(lambda i: i[1]<50,d.items()))

print(res,res1)


{'cooking oil': 80, 'chilli': 60} {'sugar': 40, 'salt': 20}



# List Comprehension


res1=[]
for i in range(1,11):
    res1.append(i)

res2=[i for i in range(1,11)]

print(res1)
print(res2)

res3=[]
for i in range(3,31,3):
    res3.append(i)

res4=[i for i in range(3,31,3)]

print(res3)
print(res4)


res5=[]
for i in range(4,41,4):
    res5.append(i)

res6=[i for i in range(4,41,4)]

print(res5)
print(res6)


[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
[4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
[4, 8, 12, 16, 20, 24, 28, 32, 36, 40]




# List

a='python programming'
l=[]
for i in a:
    if i in 'aeiouAEIOU':
        l.append(i)
print(l)
['o', 'o', 'a', 'i']


ll=[i for i in a if i in 'aeiouAEIOU']
print(ll)

['o', 'o', 'a', 'i']
['o', 'o', 'a', 'i']


'''


