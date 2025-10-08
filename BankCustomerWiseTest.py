class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.active = True
        self.atm_requested = False
        self.chequebook_requested = False
    
    def freeze_account(self):
        self.active = False
        print("Account has been frozen")

    def unfreeze_account(self):
        self.active = True
        print("Account has been unfrozen")

    def check_active(self):
        return self.active
    
class SavingsAccount(Account):
    def __init__(self, name, balance, pin, daily_limit=20000):
        super().__init__(name, balance)
        self.pin = pin
        self.daily_limit = daily_limit

    def check_balance(self, entered_pin):
        if entered_pin != self.pin:
            print(" Incorrect PIN!")
            return
        if not self.active:
            print(" Account inactive.")
            return
        print(f"Current Balance: ₹{self.balance}")

    def withdraw(self, entered_pin, amount):
        if entered_pin != self.pin:
            print(" Incorrect PIN!")
            return
        if not self.active:
            print(" Account inactive.")
            return
        if amount > self.daily_limit:
            print(" Exceeds daily withdrawal limit!")
            return
        if amount > self.balance:
            print(" Insufficient balance!")
            return
        self.balance -= amount
        print(f" Withdraw successful. Remaining Balance: ₹{self.balance}")

    def deposit(self, entered_pin, amount):
        if entered_pin != self.pin:
            print(" Incorrect PIN!")
            return
        if not self.active:
            print(" Account inactive.")
            return
        self.balance += amount
        print(f"Deposit successful. New Balance: ₹{self.balance}")

    def request_atm(self):
        if self.atm_requested:
            print(" ATM card already issued!")
        else:
            self.atm_requested = True
            print(" ATM card request successful.")

    def request_chequebook(self):
        if self.chequebook_requested:
            print("Cheque book already issued!")
        else:
            self.chequebook_requested = True
            print(" Cheque book request successful.")
            


class BusinessAccount(Account):
    def __init__(self, business_name, balance, overdraft_limit=50000):
        super().__init__(business_name, balance)
        self.overdraft_limit = overdraft_limit
        self.loan_limit = 100000


    def check_balance(self):
        print(f"Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if not self.active:
            print(" Account inactive.")
            return
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f" Withdraw successful. New Balance: ₹{self.balance}")
        else:
            print(" Withdraw exceeds overdraft limit!")

    def request_loan(self, amount):
        if not self.active:
            print(" Account inactive.")
            return
        if amount <= self.loan_limit:
            print("Loan approved.")
        else:
            print(" Loan request exceeds limit!")

    def request_chequebook(self):
        print(" Cheque book issued successfully.")

s1 = SavingsAccount("Gowthami", 10000, pin=1234)
entered_pin = int(input("\nEnter PIN to check balance: "))
s1.check_balance(entered_pin)
amount = float(input("Enter amount to withdraw: ₹"))
s1.withdraw(entered_pin, amount)
dep_amount = float(input("Enter amount to deposit: ₹"))
s1.deposit(entered_pin, dep_amount)
s1.request_atm()
s1.request_chequebook()
s1.freeze_account()
s1.unfreeze_account()

b1 = BusinessAccount("G-Tech Pvt Ltd", 50000)
b1.check_balance()
w_amount = float(input("\nEnter amount to withdraw from business account: ₹"))
b1.withdraw(w_amount)
amount = float(input("\nEnter loan amount to request: ₹"))
b1.request_loan(amount)
b1.request_chequebook()




