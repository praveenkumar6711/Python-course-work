from abc import ABC, abstractmethod

class Bankaccount(ABC):

    def checkbalance(self):
        print("You can check your balance")

    def viewhistory(self):
        print("You can see your transactions")

    def userinfo(self):
        print("You can see your details")

    def transactions(self):
        print("You can transfer money through net banking")

    @abstractmethod
    def deposite(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass


class CurrentAccount(Bankaccount):
    def deposite(self):
        print("You can deposit - CA")

    def withdraw(self):
        print("You can withdraw - CA")


class SavingAccount(Bankaccount):
    def deposite(self):
        print("You can deposit - SA")

    def withdraw(self):
        print("You can withdraw - SA")


class FixedDeposite(Bankaccount):
    def deposite(self):
        print("You can deposit - FD")

    def withdraw(self):
        print("You can withdraw - FD")


class SalaryAccount(Bankaccount):
    def deposite(self):
        print("You can deposit - SAA")

    def withdraw(self):
        print("You can withdraw - SAA")


class ZeroBalanceAccount(Bankaccount):
    def deposite(self):
        print("You can deposit - ZBA")

    def withdraw(self):
        print("You can withdraw - ZBA")


praveen = ZeroBalanceAccount()
praveen.deposite()
praveen.withdraw()
praveen.userinfo()
praveen.viewhistory()
praveen.transactions()
praveen.checkbalance()

print()

srikanth = SalaryAccount()
srikanth.deposite()
srikanth.withdraw()
srikanth.userinfo()
srikanth.viewhistory()
srikanth.transactions()
srikanth.checkbalance()

'''
You can deposit - ZBA
You can withdraw - ZBA
You can see your details
You can see your transactions
You can transfer money through net banking
You can check your balance

You can deposit - SAA
You can withdraw - SAA
You can see your details
You can see your transactions
You can transfer money through net banking
You can check your balance
'''
