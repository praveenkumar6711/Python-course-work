data = ('abc','1234')


username,password = input("Enter the username and password:").split()

if data == (username,password):
    print("Login success")
else:
    print("Login not suceess")
