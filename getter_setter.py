#Program: Demonstrates the usage of getters, setters and properties
#Author: Kai Pham
#Date: 1/28/2026


#object._Custom__private_variable  #accessing private variable outside class (not recommended)

#getters and setters


# class Customer:
#     """Customer class to keep track customers' information"""
#     def __init__(self, cust_name):
#         """initializer """
#         self.__cust_name = cust_name

#     #getter and setter
#     def get_cust_name(self):
#         return self.__cust_name
#     def set_cust_name(self, cust_name):
#         self.__cust_name = cust_name


# c = Customer("Kai Pham")

# print(c.get_cust_name())

# print(c._Customer__cust_name)




#Customer class using properties
class Customer:
    """Customer class to keep track customers' information"""
    def __init__(self, cust_name = None):
        """initializer """
        self.cust_name = cust_name

    #propertiess
    @property
    def cust_name(self):
        """get customer name"""
        return self.__cust_name
    @cust_name.setter
    def cust_name(self, cust_name):
        """set customer name"""
        if not cust_name:
            print("Customer name cannot be empty")
        else:
            self.__cust_name = cust_name



c = Customer()
c.cust_name = "Kai Pham"
print(c.cust_name)










































