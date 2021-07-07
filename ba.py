class BankAccount:
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"You deposit {amount}\n")
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"You withdraw {amount}\n")
        else:
            print (f"You have {self.balance} and tried withdrawing {amount}\n You have insufficient funds and the transaction will be cancelled\n")
        return self

    def display_account_info(self):
        print(f"Your balance is {self.balance}\n")
        return self


    def yield_interest(self):
        gained = self.balance * self.int_rate - self.balance
        self.balance = self.balance * self.int_rate
        print(f"Congrats you have gained {gained} in intrest\n")
        return self

bob = BankAccount(1.01, 2000)
alex = BankAccount(1.02, 5000)
alex.deposit(500).deposit(500).deposit(1000).withdraw(16000).yield_interest().display_account_info()
bob.deposit(100).deposit(500).withdraw(50).withdraw(50).yield_interest().display_account_info()