class Redbus:
    busno = 'cg001'
    driver_name = 'xyz'
    driver_phonenumber = 9876543210
    seats = {}
    for i in range(1,11):
        if i%2==0:
            seats[i] = 'Available'
        else:
            seats[i] = 'Booked'

    def __init__(self,name,phonenumber,age):
        self._name = name
        self._phonenumber = phonenumber
        self._age = age
        print(f"Welcome to the Redbus {self._name}. Book your bus")

    @classmethod
    def showseats(cls):
        for i in cls.seats:
            print(i,cls.seats[i])

    def booking(self,seatno):
        if Redbus.seats[seatno] == 'Available':
            Redbus.seats[seatno] = 'Booked'
            print(f'{seatno} is successfully booked')
            Redbus.driverinfo()
        else:
            print(f"{seatno} is already booked")

    @staticmethod
    def driverinfo():
        print("Driver's info")
        print("Bus no:",Redbus.busno)
        print("driver Name:",Redbus.driver_name)
        print("driver Phonenumber:",Redbus.driver_phonenumber)

'''
subbu = Redbus('subbu',8765432190,21)
subbu.showseats()
subbu.booking(2)
subbu.showseats()


Welcome to the Redbus subbu. Book your bus
1 Booked
2 Available
3 Booked
4 Available
5 Booked
6 Available
7 Booked
8 Available
9 Booked
10 Available
2 is successfully booked
Driver's info
Bus no: cg001
driver Name: xyz
driver Phonenumber: 9876543210
1 Booked
2 Booked
3 Booked
4 Available
5 Booked
6 Available
7 Booked
8 Available
9 Booked
10 Available

'''
