#Program: This program demostrates class creation
#Author: Kai Pham
#Date: 1/28/2026
from os import name


class StudentAverage ():
    """ StudentAverage class calculates students' semester average """
    # def __new__(cls, ):
    #     """Create new instance"""
    #     return super().__new__(cls)
    
    #getters
    #setters
    #methods
    def __init__(self, name, grades):
        """initializer (constructor) """
        self.name = name
        self.grades = grades
    def calculate_average(self):
        """Calculate the average of the grades"""
        return sum(self.grades) / len(self.grades)
    
    def calc_letter_grade(self):
        """Calculate letter grade based on average"""
        average = self.calculate_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'



    def __str__(self) :
        """Display object"""
        return f'Student Name: {self.name}\tGrades: {self.grades}\tAverage: {self.calculate_average():.2f}\tLetter Grade: {self.calc_letter_grade()}'

#end of your class




#test class - create instance (object) 
if __name__ == '__main__':
    student_1 = StudentAverage('John', [85, 90, 78, 92])
    print(student_1)