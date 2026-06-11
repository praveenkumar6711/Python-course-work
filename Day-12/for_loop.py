'''
seq: str,list,tuples,set,dict,range
for i in seq:
    #statements
   
name = "Python"

for i in name:
    print(i)


pin = 1234

for i in range(5):
    e_pin = int(input("Enter the pin: "))

    if e_pin == pin:
        print("Unlock the phone")
        break
    else:
        print("Incorrect Password")
else:
    print("Try again after 60 sec")



l=[2,3,5,6,7,8,11,34,56]

search= int(input("Enter the elements:"))

for i in range(len(l)):
    if l[i] == search:
        print(f'{search} is found at index-[i]')
        break
else:
    print(f'{search} is not found')

    # strong password or not


    Adfgjhdfjh@123
    adbshahvfh1234
    56565656
    @@#$%Z&

  
password=input("Enter the password :")
if len(password)>=8:
    s=set()
    for i in password:
        if i.isupper():
            s.add('u')
        elif i.islower():
            s.add('l')
        elif i.isdigit():
            s.add('d')
        else:
            s.add('s')

    if len(s)==4:
        print("Strong password")
    else:
        print("Weak password")
else:
    print("Weak password")


status = "None"

assert status != None, "You need to update the status"
print(status)


status = "Active"

assert status != None, "You need to update the status"
print(status)



name='abc'
batch=55
age=21

assert {name!= None and batch!=None and age!=None}, "You need to update the status"
print(name,batch,age)



i = 1

while i <= 5:
    print(i)
    i += 1


'''





