#Program: This program demonstrates the class inheriance
#Author: Kai Pham
#Date: 2024-06-10

class BankAccount:
    """ BankAccount class keeps track the banking activity"""
    def __init__(self, account_no, balance=0.0):
        """ initializer"""
        self.account_no = account_no
        self.balance = balance
    @property
    def account_no(self):
        return self._account_no
    @account_no.setter
    def account_no(self, account_no):
        if not account_no:
            print("Unassigned account number.")
            self._account_no = ""
        else:
            self._account_no = account_no

    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, balance):
        if balance < 0.0:
            print("Cannot have negative balance.")
            self._balance = 0.0
        else:
            self._balance = balance

    # methods
    def deposit(self, amount):
        """ deposit money into account """
        if amount <= 0.0:
            print("Cannot deposit negative or 0 amount.")
        else:
            self.balance += amount
    def withdraw(self, amount):
        """ withdraw money from account """
        if amount <= 0.0:
            print("Cannot withdraw negative or 0 amount.")
        elif amount > self.balance:
            print("Cannot withdraw more than the balance.")
        else:
            self.balance -= amount

    def __str__(self):
        return f'Account NO: {self.account_no}\nBalance: ${self.balance:.2f}'



class CheckingAccount(BankAccount):
    """ CheckingAccount class inherits from BankAccount class """
    def __init__(self, account_no, balance=0.0, checks=0):
        """ initializer """
        super().__init__(account_no, balance)
        self.checks = checks
    @property
    def checks(self):
        return self._checks
    @checks.setter
    def checks(self, checks):
        if checks < 0:
            print("Cannot have negative checks.")
            self._checks = 0
        else:
            self._checks = checks

    def check_fee (self):
        """ calculate check fee """
        if self.checks < 20:
            return self.checks * 0.08
        elif self.checks < 50:
            return self.checks * 0.06
        else:
            return self.checks * 0.03



    def __str__(self):
        return (f'Checking account:\n{super().__str__()}\nTotal Checks: {self.checks}\nCheck Fee: ${self.check_fee():.2f}'
                f'\nFinal Balance: ${self.balance - self.check_fee():.2f}')
    
class SavingsAccount(BankAccount):
    """Saving Account class to keep track the saving acitivity"""
    def __init__ (self, account_no, balance, interest_rate):
        """ initializer """
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate
    @property
    def interest_rate(self):
        return self._interest_rate
    @interest_rate.setter
    def interest_rate(self, interest_rate):
        if interest_rate < 0.0:
            print("Interest rate cannot be negative.")
            self._interest_rate = 0.0
        else:
            self._interest_rate = interest_rate
    # methods
    def interest(self):
        """ add interest to the account """
        return self.balance * self.interest_rate / 12
    
    def __str__(self):
        return (f"Saving account:\n{super().__str__()}\nInterest Rate: {self.interest_rate}"
                f"\nInterest earned: ${self.interest():.2f}\nFinal Balance: ${self.balance + self.interest():.2f}"       
                )








#test classes
if __name__ == "__main__":
    checking1 = CheckingAccount("js_1", 1000.0, 10)
    checking1.deposit(500.0)
    checking1.withdraw(50.0)
    
    savings = SavingsAccount('saving_1', 1000.0, 0.05)
    

    checking1.deposit(500.0)
    checking1.withdraw(100.0)


    accounts = [checking1, savings]
    for account in accounts:
        print(account)
        print()