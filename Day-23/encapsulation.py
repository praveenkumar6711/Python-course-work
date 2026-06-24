
'''
# Encapsulation:

Encapsulation is the process of wrapping data (attributes) and methods into a single unit (class) and restricting direct access to data.



class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers =[]
        print(f"Welcome to the instagram,{self.username}")


praveen= Instagram("praveen","Praveen@123")


  # OUTPUT: Welcome to the instagram,praveen

'''


class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.followers =[]

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self__password = newpassword
        


praveen= Instagram("praveen","Praveen@123")

print("Before username:",praveen.username)
praveen.username = 'praveenkumar'
print("After username:",praveen.getpassword())
print("Afer 
praveen.setpassword('praveenkumar@123')
print("After password:",praveen.getpassword())

#OUTPUT:

Before username: praveen
After username: Praveen@123
After username: Praveen@123

'''

