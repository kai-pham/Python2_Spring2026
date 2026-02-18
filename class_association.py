# Program: This program demonstrates class association between two objects (Invoice, Item)
# Author: Kai Pham
# Date: 2024-06-10

class Item:
    """ Item class to keep track the inventory of one item """
    # init
    def __init__(self, name='',qty=0,unit_price=0.0):
        """ initializer/constructor """
        self.name = name
        self.qty = qty
        self.unit_price = unit_price
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self, name):
        if not name:
            print("Unassigned item name.")
            self._name=""
        else:
            self._name=name
    @property
    def qty(self):
        return self._qty
    @qty.setter
    def qty(self,qty):
        if qty <= 0:
            print("Cannot have negative or 0 qty.")
            self._qty = 0
        else:
            self._qty = qty
    @property
    def unit_price(self):
        return self._unit_price
    @unit_price.setter
    def unit_price(self, unit_price):
        if unit_price <= 0.0:
            print("Cannot have negative or 0 qty.")
            self._unit_price = 0.0
        else:
            self._unit_price = unit_price
    
    # methods
    def calc_item_price(self):
        """ calculate item price """
        return self.qty * self.unit_price
    def __str__(self):
        """ display object """
        return f'{self.name:<15}{self.qty:>3}{self.unit_price:>12.2f}{self.calc_item_price():>12.2f}'

import datetime

class Invoice:
    """ Invoice class keeps track the invoice info """
    def __init__(self, customer,inv_no):
        """ initializer """
        self.customer = customer
        self.inv_no = inv_no
        self.inv_date = datetime.datetime.now()
        self.items = []
    # add property here

    # methods
    def add_item(self,item):
        """ add item object to item list (items)"""
        if isinstance(item,Item):
            self.items.append(item)
        else:
            print("Incorrect item object.")
    def remove_item(self, item):
        """ remove item object from item list (items)"""
        if isinstance(item, Item):
            if item in self.items:
                self.items.remove(item)
            else:
                print("Item does not in the invoice items")
        else:
            print("Incorrect item object.")
    
    def calc_grand_total(self):
        """ calculate the invoice total """
        total = 0.0
        for item in self.items:
            total += item.calc_item_price()
        return total
    
    def __str__(self):
        """ display invoice object """
        date_string = self.inv_date.strftime("%m/%d/%Y")
        return f"Customer:{self.customer}\tInv No:{self.inv_no}\tInv Date:{date_string}"

# test classes
if __name__ == '__main__':
    item1 = Item('Scanner',2,65.0)
    item2 = Item('Printer',25, 89.5)
    item3 = Item('Boxes',10,3.5)

    inv1 = Invoice("John Smith","inv_0211")
    inv1.add_item(item1)
    inv1.add_item(item2)
    inv1.add_item(item3)

    print(inv1)
    print(f"{"Item Name":<15}{"qty":<5}{"Unit Price":<12}{"Item Price":<12}")
    for item in inv1.items:
        print(item)
    print(f"Invoice total: ${inv1.calc_grand_total():,.2f}")