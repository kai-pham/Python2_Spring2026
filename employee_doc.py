class Employee:
    def __init__(self, name, dept):
        """ initializer """
        self.name = name
        self.dept = dept

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            print("Unassigned employee name.")
            self._name = ""
        else:
            self._name = name

    @property
    def dept(self):
        return self._dept
    @dept.setter
    def dept(self, dept):
        if not dept:
            print("Unassigned employee department.")
            self._dept = ""
        else:
            self._dept = dept
    def pay(self):
        return 0.0       
            

    def __str__(self):
        return f'Employee Name: {self.name}\t Department: {self.dept}'


class HourlyPaid (Employee):
    def __init__(self, name, dept,hours ,hourly_rate):
        """ initializer """
        super().__init__(name, dept)
        self.hourly_rate = hourly_rate
        self.hours = hours

    @property
    def hourly_rate(self):
        return self._hourly_rate
    @hourly_rate.setter
    def hourly_rate(self, hourly_rate):
        if hourly_rate <= 0.0:
            print("Cannot have negative or 0 hourly rate.")
            self._hourly_rate = 0.0
        else:
            self._hourly_rate = hourly_rate


    @property
    def hours(self):
        return self._hours
    @hours.setter
    def hours(self, hours):
        if hours < 0:
            print("Cannot have negative hours.")
            self._hours = 0
        else:
            self._hours = hours
        
    #methods
    def pay(self):
        """ calculate pay for hourly paid employee """
        if self.hours < 0:
            print("Cannot have negative hours.")
            return 0.0
        elif self.hours> 40:
            return 40 * self.hourly_rate + (self.hours - 40) * self.hourly_rate * 1.5
        else:
            return self.hours * self.hourly_rate
    def __str__(self):
        return f'Hourly Paid Employee:\n{super().__str__()}\nHourly Rate: ${self.hourly_rate:.2f}'
    

if __name__ == "__main__":
    emp1 = Employee("John Smith", "IT")
    print(emp1)
    print()

    hourly_emp1 = HourlyPaid("John Smith", "IT", 35.0, 15.0)
    print(hourly_emp1)
    print(f'Pay for 35 hours: ${hourly_emp1.pay():.2f}')

    print()

    emp2 = Employee("Jane Doe", "HR")
    print(emp2)
    print()

    hourly_emp2 = HourlyPaid("Jane Doe", "HR", 45.0, 20.0)
    print(hourly_emp2)
    print(f'Pay for 45 hours (overtime): ${hourly_emp2.pay():.2f}')
        
        
    