
'''
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



l=[val for var in seq]
l=[var for var in seq if condition]
l=[var if condition else val for var in seq]


a=[1,2,3,4,5,6,7,8,9,10]
l=[]
for i in a:
    if i%2==0:
        l.append(i)
    else:
        l.append(0)
print(l)


ll=[i if i%2==0 else 0 for i in a]
print(ll)

[0, 2, 0, 4, 0, 6, 0, 8, 0, 10]
[0, 2, 0, 4, 0, 6, 0, 8, 0, 10]





l=[int(input(f'Enter the number - {i+1}:')) for i in range(10)]
print(l)


Enter the number - 1:22
Enter the number - 2:33
Enter the number - 3:44
Enter the number - 4:55
Enter the number - 5:66
Enter the number - 6:77
Enter the number - 7:88
Enter the number - 8:99
Enter the number - 9:11
Enter the number - 10:56
[22, 33, 44, 55, 66, 77, 88, 99, 11, 56]



# Nested List

l=[]
for i in range(3):
    for j in range(1,4):
        l.append(j)

print(l)

ll=[j for i in range(3) for j in range (1,4)]

print(ll)


[1, 2, 3, 1, 2, 3, 1, 2, 3]
[1, 2, 3, 1, 2, 3, 1, 2, 3]





l = []

for i in range(3):
    temp = []
    for j in range(1, 4):
        temp.append(j)
    l.append(temp)

print(l)
ll = [[j for j in range(1, 4)] for i in range(3)]

print(ll)


[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]



s=set()
for i in range(1,11):
    s.add(i)
s1=[i for i in range(1,11)]

print(s,s1)

{1, 2, 3, 4, 5, 6, 7, 8, 9, 10} [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


d={}
for i in range(1,11):
    d[i]=i*i

print(d)

res = {i:i*i for i in range(1,11)}
print(res)

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}



# 5 marks

res = {input('Enter the names: '):int(input("Enter the marks: ")) for i in range(5)}
print(res)

Enter the names: praveen
Enter the marks: 45
Enter the names: subbu
Enter the marks: 46
Enter the names: ravi
Enter the marks: 45
Enter the names: raju
Enter the marks: 85
Enter the names: uday
Enter the marks: 56
{'praveen': 45, 'subbu': 46, 'ravi': 45, 'raju': 85, 'uday': 56}


'''
