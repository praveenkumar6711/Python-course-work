
'''
for var in seq:
    print(var)

s='python programming '
for ch in s:
    print(ch)

l=['sugar','salt','oil']
for item in l:
    print(item)
    


t={'1.laptop','2.mouse','3.keyboard'}
for i in t:
    print(i)


s={'laptop','mouse','keyboard'}
for i in s:
    print(i)
    


d={'name':'subbu','batch':55,'course':'PfS'}
for i in d:
    print(i,d[i])




# range(start,stop1,stop+1,step)=> (0,n,-1)

for i in range(1,11):
    print(i)


for i in range(2,51,2):
    print(i)




for i in range(5,101,5):
    print(i)


for i in range(20,0,-1):
    print(i)
    


for i in range(2,11,2):
    print(i)

    
for i in range(9,91,9):
    print(i)


for i in range(6):
    print(i)



for i in range(4,30,4):
    print(i)



#  looping statements

s='looping'
for i in enumerate(s):
    print(i[0],i[1])

l=(7,2,3,4,5,6,6,67)
for i in range(len(l)):
    print(i,l[i])
    


l=(7,2,3,4,5,6,6,67)
for i in range(len(l)):
               print(i)

k={7,2,3,4,5,6,6,67}
for i in enumerate(k):
    print(i[0],i[1])



for i in range(10):
    pass


for i in range (10):
    if i==5:
        break
    print(i)


    
for i in range (30):
    if i==35:
        break
    print(i)




for i in range (15):
    if i==10:
        continue
    print(i)


   


s="looping statements"
for i in s:
    if i in 'aeiouAEIOU':
        print(i)


l=[56,66,76,845,34,8,9,90,35]
for i in l:
    if i%2==0:
        print(i)


d={'Laptops':0,'chargers':2,'keyboard':10,'phone':15,'tab':0,'mouse':5}

for i in d:
    if d[i]:
        print(i)



t=(9,2,13,4,5,6)

for i in range(len(t)):
    print(i*t[i])
'''
names = {'praveen', 'kumar', 'sunny', 'bunty'}

for i in names:
    print(i.upper())






