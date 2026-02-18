#Program: This program demonstrates how operator overloading works
#Author: Kai Pham
#Date: 2024-06-10

class Number:
    """Number class shows how operator overloads"""
    def __init__(self, value):
        """Initializer"""
        self.value = value


    # getter and setter
    
    # def get_value(self):
    #     return self.__value
    # def set_value(self, value):
    #     self.__value = value
    
    
    
    @property
    def value(self):
        """get value info"""
        return self.__value

    @value.setter
    def value(self, value):
        """set value info"""
        self.__value = value

    #methods
    def __add__(self, other):
        """rewrite the add method"""
        return Number(self.value + other.value)
    def __eq__(self, other):
        """rewrite the equal method"""
        return self.value == other.value
    def __gt__(self, other):
        """rewrite the greater than method"""
        return self.value > other.value
    def __str__(self):
        """display object"""
        return f"Value = {self.value}"
    

#test class
num1 = Number(10)
num2 = Number(20)
num3 = num1 + num2
print(f"num1: {num1}\nnum2: {num2}\nnum3: {num3}")
print(f"num1 == num2: {num1 == num2}")
print(f"num1 > num2: {num1 > num2}")
print(f"num2 > num1: {num2 > num1}")