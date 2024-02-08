class bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, money):
        self.balance += money
        print(f"Владелец: {self.owner}; Баланс: {self.balance}")
    def withdraw(self, money):
        if(money <= self.balance):
            self.balance -= money
            print("Withdraw accepted")
        else:
            print("Withdraw can not be accepted")
    def check (self):
        print(f"Владелец: {self.owner}; Баланс: {self.balance}")

acc1 = bank("GGG", 555555555)
acc1.deposit(5)
acc1.withdraw(2)
acc1.check()
acc1.withdraw(2000000000000000)
acc1.check()
        