#Program: This program demonstrates the usage of property
#Author: Kai Pham
#Date: 2024-06-10


class Invoice:
    """Invoice class to keep track the invoice details"""
    def __init__(self, customer, amount):
        """initializer """
        self.customer = customer
        self.amount = amount

    #properties
    @property
    def customer(self):
        """get customer info"""
        return self.__customer
    @customer.setter
    def customer(self, customer):
        self.__customer = customer
    @property
    def amount(self):
        """get amount info"""
        return self.__amount
    @amount.setter
    def amount(self, amount):
        if not isinstance(amount, (int, float)):
            print("Invalid type of amount")
        elif amount < 0:
            print("Amount cannot be negative")
            self.__amount = 0
        else:
            self.__amount = amount
    def __str__(self):
        """display object"""
        return f"Customer:{self.customer}\t Amount:{self.amount:.2f}"


#test_class

inv1 = Invoice("Kai Pham", 250.75)
inv2 = Invoice("Anna Smith", -100)  #invalid amount
print(inv1)
print(inv2)






















