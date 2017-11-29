
class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


#Creates a subclass of the base account.
class Savings(Account):
    """ Docstring description can be seen through Savings.__doc__
    Good to put a description here"""

    def __init__(self, filepath, fee):
        self.fee = fee
        Account.__init__(self, filepath)

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee



"""account = Account("balance.txt")

print (account.balance)
account.deposit(100)
print (account.balance)
account.commit()"""

savings = Savings("balance.txt", 1)

print(savings.balance)
savings.transfer(100)
print(savings.balance)
savings.commit()
