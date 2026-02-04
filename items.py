#Program: This program keeps track for the inventory of a particular item
#Author: Kai Pham
#Date: 1/28/2026

class Item:
    """Item class to keep track the inventory of a particular item"""
    def __init__(self, name='', qty=0, unit_price=0.0) -> None:
        """initializer (constructor) """
        self.name = name
        self.qty = qty
        self.unit_price = unit_price
    #getters
    #setters
    #methods
    def calc_item_price(self):
        """Calculate total price of the item based on quantity and unit price"""
        return self.qty * self.unit_price
    def __str__(self) :
        """Display object"""
        return f'Item Name: {self.name}Quantity: {self.qty}Unit Price: ${self.unit_price:.2f}Total Price: ${self.calc_item_price():.2f}'

#test class
if __name__ == "__main__":
    item_1 = Item('Printer', 10, 799.99)
    item_2 = Item('Scanner', 5, 50.5)
    item_3 = Item()
    item_3.name = 'Pens'
    item_3.qty = 100
    item_3.unit_price = 1.5
    items = [item_1, item_2, item_3]
    for item in items:
        print(item)
        print('-------------------')

    total_price = 0.0
    for item in items:
        total_price += item.calc_item_price()
    print(f'Total inventory price: ${total_price:.2f}')