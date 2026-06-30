'''
#FILE HANDING:
   -open
   - read
   -write
   
#seek: points towards starting



file=open('sample.txt','r')


print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())

file.close()


Names:

praveen
Srikanth
Chanakya
pradeep
Names:

['Names:\n', '\n', 'praveen\n', 'Srikanth\n', 'Chanakya\n', 'pradeep']



#using exception handing

try:
    file=open('samplee.txt','r')

except FileNotFoundError:
    print("File is not there")

else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())

    file.close()


File is not there
#file name error




try:
    file=open('sample.txt','r')

except FileNotFoundError:
    print("File is not there")

else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())

    file.close()

Names:

praveen
Srikanth
Chanakya
pradeep
Names:

['Names:\n', '\n', 'praveen\n', 'Srikanth\n', 'Chanakya\n', 'pradeep']



#open

with open('sample.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())




#Append

with open('sample.txt','a') as file:
    file.write('\npraneeth\nshiva\nkumar')





#create
with open('samples.txt','a') as file:
    file.write('\npraneeth\nshiva\nkumar')

#creating in another file

#write

with open('sample.txt','w') as file:
    file.write('\npraneeth\nshiva\nkumar')

praneeth
shiva
kumar

#remove all existing details and rename




with open('demo.txt','w+') as file:
    file.write('\npraneeth\nshiva\nkumar')
    file.seek(0)
    print(file.read())

#creating another file with the write

'''



import os
#os.mkdir('smaple')

os.rmdir('smaple')


Traceback (most recent call last):
  File "C:/Users/prave/OneDrive/Desktop/Python-course-work/Day-27/filehandling.py", line 141, in <module>
    os.rmdir('smaple')
PermissionError: [WinError 5] Access is denied: 'smaple'
























    
