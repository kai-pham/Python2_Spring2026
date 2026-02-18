#Program: This program tracks customer reward for a retail store
#Author: Kai Pham
#Date: 2024-06-18


class CustomerReward():
    """CustomerReward class to track reward for different types of customers"""
    def __init__(self,customer, purchase):
        """ initializer """
        self.customer = customer
        self.purchase = purchase
    @property
    def customer(self):
        """get customer info"""
        return self._customer
        
    @customer.setter
    def customer(self, customer):
        if not customer:
            print("Unassigned customer name.")
            self._customer = ""
        else:
            self._customer = customer

    @property
    def purchase(self):
        """get purchase amount"""
        return self._purchase
    
    @purchase.setter
    def purchase(self, purchase):
        if purchase < 0.0:
            print("Cannot have negative purchase amount.")
            self._purchase = 0.0
        else:
            self._purchase = purchase
    
    #methods
    def calc_reward(self):
        return 0.0
    def __str__(self):
        return f'Customer: {self.customer}\t Purchase: {self.purchase}'
    
















class CorporateCustomerReward(CustomerReward):
    """CorporateCustomer tracks the reward for the corporate customers"""
    def __init__(self, customer, purchase, contact):
        """ initializer """
        super().__init__(customer, purchase)
        self.contact = contact

    @property
    def contact(self):
        """get contact info"""
        return self._contact

    @contact.setter
    def contact(self, contact):
        if not contact:
            print("Unassigned contact info.")
            self._contact = ""
        else:
            self._contact = contact
    
    #method
    def calc_reward(self):
        if self.purchase <300.0:
            return 0.0
        elif self.purchase < 1000.0:
            return self.purchase * 0.02
        else:
            return self.purchase * 0.04

    def __str__(self):
        """display object"""
        return f'Corporate Customer:\n {super().__str__()}\n Contact: {self.contact}\t Reward: {self.calc_reward()}'






    
class RetailCustomerReward(CustomerReward):
    """RetailCustomer tracks the reward for the retail customers"""
    def __init__(self, customer, purchase, email):
        """ initializer """
        super().__init__(customer, purchase)
        self.email = email

    @property
    def email(self):
        """ return email """
        return self._email
    @email.setter
    def email(self, email):
        if not email:
            print("Unassigned email.")
            self._email = ""
        else:
            self._email = email

    #method
    def calc_reward(self):
        if self.purchase < 20.0:
            return 0.0
        elif self.purchase < 100.0:
            return self.purchase * 0.03
        else:
            return self.purchase * 0.05

    def __str__(self):
        """display object"""
        return f'Retail Customer:\n {super().__str__()}\n Email: {self.email}\t Reward: {self.calc_reward()}'


if __name__ == "__main__":
    corporate1 = CorporateCustomerReward("ABC Company", 1500.0, "John Doe")
    corporate2 = CorporateCustomerReward("XYZ Company", 500.0, "Jane Smith")
    retail1 = RetailCustomerReward("John Smith", 150.0, "johnsmith@gmail.com")
    retail2 = RetailCustomerReward("Jane Doe", 50.0, "janedoe@gmail.com")
    
    
    rewards = [corporate1, corporate2, retail1, retail2]
    for reward in rewards:
        print(reward)
        print()