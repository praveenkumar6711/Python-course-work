'''
#syntax

var= lambda agr: exp


add = lambda a,b:a+b

print(add(12,13))
print(add(12,33))

25
45




wish=lambda name:f'welcome the python course {name}'

print(wish('subbu'))
print(wish('praveen'))


welcome the python course subbu
welcome the python course praveen



gst=lambda price:price+price*0.18

print(gst(1000))
print(gst(6000))
print(gst(4550))


1180.0
7080.0
5369.0




greatest=lambda a,b: a if a>b  else b

print(greatest(45,12))
print(greatest(8000,9000))
print(greatest(7879,545674))

45
9000
545674




iseven= lambda a: f'{a}-Even number' if a%2==0 else f'{a}-odd number'

print(iseven(4))
print(iseven(85))
print(iseven(99))


4-Even number
85-odd number
99-odd number



bill= lambda charge:charge if charge>90 else charge +40

print(bill(200))
print(bill(40))
print(bill(10))

200
80
50

#length of the string

length= lambda text: len(text)

print(length("Praveen"))

7


# nested if else

login=True
instock=False

status= lambda login,instock: ("You can buy product" if instock else "Product is out of stock") if login else "Login to buy a product"

print(status(login,instock))

#largest number

largest= lambda a,b: a if a>b  else b

print(largest(10,20))

20



#list

l=[1,2,3,4,5,6,7]
res=list(map(lambda i:i**3,l))

print(res)

[1, 8, 27, 64, 125, 216, 343]



names={"praveen","nagender","rohith"}
t=list(map(lambda i:i.title(),names))
print(t)

['Nagender', 'Praveen', 'Rohith']

# FILTER:

l=[1,2,3,4,5,6,7,8,9,10,11,12]
res= list(filter(lambda i:i%2==0,l))
print(res)

[2, 4, 6, 8, 10, 12]


l=[1,2,3,4,5,6,7]
res= list(filter(lambda i:i>5,l))
print(res)


[6, 7]



l=[1,2,3,4,5,6,7]
res= list(filter(lambda i:i%3==0,l))
print(res)

[3, 6]


#Reduce Function

from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10,11,12]
s=reduce(lambda sum ,i: sum+i,l)
p=reduce(lambda pro,i: pro*i,l)

print(l,s,p)

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 78 479001600


from functools import reduce

l=[1,2,3,4,5,6,7,8,9,10,11,12]

s=reduce(lambda sum ,i: sum+i,l)
p=reduce(lambda pro,i: pro*i,l)
n=reduce(lambda max,i:max if max>i else i,l)
mi=reduce(lambda max,i:max if max<i else i,l)
print(s,p,n,mi)

78 479001600 12 1

'''


d={'praveen':60,'nani':45,'pradeep':60,'ajay':80}

print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))

print(dict(sorted(d.items(),reverse='True')))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))

{'ajay': 80, 'nani': 45, 'pradeep': 60, 'praveen': 60}
{'nani': 45, 'praveen': 60, 'pradeep': 60, 'ajay': 80}
{'praveen': 60, 'pradeep': 60, 'nani': 45, 'ajay': 80}
{'ajay': 80, 'praveen': 60, 'pradeep': 60, 'nani': 45}





