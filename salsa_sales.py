#Program: This program keeps track of the salsa sales for a store
#Author: Kai Pham
#Date: 1/28/2026

class SalsaSales:
    """SalsaSales class to keep track of different flavors of sales for a store"""
    def __init__(self, flavor, jars_sold=0, unit_price=0.0) -> None:
        """initializer (constructor) """
        self.flavor = flavor
        self.jars_sold = jars_sold
        self.unit_price = unit_price
    #getters & setters
    #methods
    def calc_total_sales(self):
        """Calculate total sales based on jars sold and unit price"""
        return self.jars_sold * self.unit_price
    
    def __str__(self) :
        """Display object"""
        return f'Salsa Flavor: {self.flavor:10s}\nJars Sold: {self.jars_sold:10d}\nUnit Price: ${self.unit_price:12.2f}\nTotal Sales: ${self.calc_total_sales():.2f}'
    
#test class
if __name__ == "__main__":
    mild = SalsaSales('Mild', 20, 3.5)
    medium = SalsaSales('Medium', 30, 4.0)
    hot = SalsaSales('Hot', 10, 5.0)
    zesty = SalsaSales('Zesty', 60, 6)
    salsas = [mild, medium, hot, zesty]
    total_sales = 0.0
    for salsa in salsas:
        total_sales += salsa.calc_total_sales()
        print(salsa)
        print('-------------------')
    print(f'Total salsa sales: ${total_sales:.2f}')