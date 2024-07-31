# Question 1

''' In this question, person class is to be made with attributes first name, last name and age.
    There will be constructor that will intialize data members of class and get_info() function will
    print attributes on console screen. Class student will reuse Person class by inheritance and there will be 
    additional member named as student id that will let us know about student id and get_info will be overrided to
    print student id. Employee class will also inherit Person class and two additional members wil there be 
    as salary and number and get_info overrided to print these. Inheritance used heirarichal as Person class
    is inherited by Childs Student and Employee class. In main function, objects of student and employee class
    will be made to print information passed in their objects.'''
class Person:
    """
    The Person class stores information about a person and has a get_info method to print his/her information.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes the attributes first_name, last_name, and age using constructor.
        """
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age
        
    '''Function to print information of a person'''
    def get_info(self):
        """
        Prints the full name and age of the person.
        """
        print("Full Name:", self.first_name, self.last_name)
        print("Age:", self.age)

class Student(Person):
    """
    The Student class inherits attributes and methods from the Person class and adds a student_id attribute to Student Class.
    """
    def __init__(self, first_name, last_name, age, student_id):
        """
        Initializes the attributes of the Student class including the inherited ones from the Person class.
        """
        super().__init__(first_name, last_name, age)
        self.student_id=student_id

    def get_stuinfo(self):
        """
        Prints the full name, age of the student using the get_info() method from the Person class and Student Id from Student Class.
        """
        super().get_info()
        print("Student ID:", self.student_id)

class Employee(Person):
    """
    The Employee class inherits attributes and methods from the Person class and adds employee_number and salary attributes.
    """
    def __init__(self, first_name, last_name, age, employee_number, salary):
        """
        Initializes the attributes of the Employee class including the inherited ones from the Person class.
        """
        super().__init__(first_name, last_name, age)
        self.employee_number  = employee_number
        self.salary           = salary

    def get_empinfo(self):
        """
        Prints the full name, age, employee number, and salary of the employee using the get_info() method from the Person class.
        """
        super().get_info()
        print("Employee No:", self.employee_number)
        print("Salary:", self.salary, "USD")
        
    """ Driver Code with main function"""
def main():
    """
    Creates instances of Student and Employee classes and calls their respective methods to print information.
    """
    new_student = Student("Anthony", "Smith", 35, "s346571")
    new_student.get_stuinfo()
    
    # Add a separator using # sign
    print("="*22)

    new_employee = Employee("Sarah", "Taylor", 34, 2919736, 5000)
    new_employee.get_empinfo()
    
    """Call the Main function"""
if __name__ == "__main__":
    main()
