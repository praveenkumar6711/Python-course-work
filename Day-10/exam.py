'''
n= list(map(int,input().split()))

print("Length:",len(n))
print("Sorted:",sorted(n))
print("maximum:",max(n))
print("minimum:",min(n))
'''
'''
salary=int(input())
bonus=0

if salary >=70000:
    bonus=salary *0.2
elif salary >=50000:
    bonus=salary *0.15
elif salary >=70000:
    bonus=salary *0.2
elif salary >= 30000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

print("Bonus :", bonus)

'''

'''
tup = tuple(input("Tuple: ").split())

product = input("Products: ")
price = int(input("Prices: "))

s = set(map(int, input("set values : ").split()))

d = {product: price}
d=()


print("Tuple :", tup)
print("Dictionary :", d)
print("Set :", s)

'''
'''
age = int(input())

if age >= 18:
    print("Eligible for Voting")
else:
    print("Not Eligible for Voting")
 '''


marks = int(input())

if marks >= 35:
    print("Pass")
else:
    print("Fail")
