data = {
    'subbu': {'status': True, 'python': 90, 'mysql': 95, 'flask': 94},
    'nagender': {'status': True, 'python': 70, 'mysql': 66, 'flask': 84},
    'dinesh': {'status': False, 'python': None, 'mysql': None, 'flask': None},
    'praveen': {'status': True, 'python': 68, 'mysql': 55, 'flask': 64},
    'suresh': {'status': True, 'python': 33, 'mysql': 25, 'flask': 34},
}

name = input("Enter the name: ")

if name in data:
    if data[name]['status']:
        total = data[name]['python'] + data[name]['mysql'] + data[name]['flask']
        avg = total / 3

        if avg > 90:
            print(f"Congratulations {name}, you got First Class!!!")
        elif avg > 70:
            print(f"Good {name}, keep it up for the next time!!")
        elif avg > 35:
            print(f"Better {name}, work hard for the next time!!")
        else:
            print(f"{name}, you have failed in the exam. Bring your parents.")
    else:
        print(f"{name} didn't write the exam. Bring your parents.")
else:
    print(f"{name} data is not found.")
