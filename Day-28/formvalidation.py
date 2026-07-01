
'''
import re
pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

text = input("Enter the text:: ")
res = re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid Format")


Enter the text:: praveen.132
Invalid Format



#phone number validation

import re

pattern = r'^(?:\+91|0)?[6-9]\d{9}$'


text=input("Enter the text: ")

res=re.fullmatch(pattern,text)

print("Valid format" if res else "Invalid Format")


Enter the text: 7875215245
Valid format

Enter the text: 656949852
Invalid Format




#validation of password:


import re

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'

password = input("Enter password: ")

if re.fullmatch(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")




Enter password: Kumar@123
Valid Password

Enter password: kumar@123
Invalid Password


'''





























