# Program: This program test SalsaSales class to make sure the logic is correct
# Author: Kai Pham
# Date: 1/28/2026
from salsa_sales import SalsaSales

def main():
    """main function"""
    flavors = ['mild', 'medium', 'hot', 'zesty']
    salsa_objects = []

    for flavor in flavors:
        salsa_object = SalsaSales()
        update_sales(flavor, salsa_object)
        salsa_objects.append(salsa_object)
    display_report(salsa_objects)    



def update_sales(flavor, salsa_object):
    """Get user input for salsa price and jars sold based on the flavor"""
    qty = int(input(f'Enter jars sold for {flavor} flavor: '))
    while qty < 0:
        qty = int(input(f'Jars sold must be greater than 0. Re-enter jars sold for {flavor} flavor: '))
    price = float(input(f'Enter unit price for {flavor} flavor: '))
    while price < 0:
        price = float(input(f'Unit price must be greater than 0. Re-enter unit price for {flavor} flavor: '))

    salsa_object.flavor = flavor
    salsa_object.jars_sold = qty
    salsa_object.unit_price = price




def display_report(salsa_objects):
    """Display the final report"""

    print(f'\n{"Flavors":10s}{"Jars Sold":>10s}{"Unit Price":>12s}{"Total Sales":>12s}')
    for salsa in salsa_objects:
        print(salsa)
    total_sales = calc_total_sales(salsa_objects)
    print(f'Total salsa sales: ${total_sales:.2f}')



def calc_total_sales(salsa_objects):
    """Calculate the total salsa sales"""
    total = 0.0
    for salsa in salsa_objects:
        total += salsa.calc_total_sales()

    return total

#call main
main()
