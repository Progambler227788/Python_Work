# Question 1
'''In this question, there will be student class having passing marks set to 50, name and marks are attributes.
__str__ will return string having name and marks of students so that it can be printed on screen when we call
object like print(student1). passOrFail function will return pass in case student marks are greater than or equal to
marks defined in passing marks variable default value seems to be set of 50. It can be changed later to either
60 or 70 depending on crieteria of passing. At last after definition of class, students objects are instantiated and
values are passed in them to test functinality of pass or Fail function.'''
class Student:
    """
    The Student class represents a student having name and marks as his/her attributes.
    It also includes passingMark variable having value of 50 as default passing marks
    """
    passingMark=50  # Class variable for passing marks

    def __init__(self, name, mark):
        """
        initializes an object with name and marks
        """
        self.name = name
        self.mark = mark

    def __str__(self):
        """
        This function will return a String having name and marks 
        """
        return f"Name: {self.name}, Mark: {self.mark}"

    def passOrFail(self):
        """
        This function will return 'Pass' as a String if the mark is greater than or equal to passingMark,
        otherwise returns 'Fail' as a String.
        """
        if self.mark >= Student.passingMark:
            return "Pass"
        # When if is false, then it will be returned as Fail
        return "Fail"

# Outside the class
student1 = Student('John', 52)  # Instantiate student1 object
status1 = student1.passOrFail()  # Call passOrFail method for student1

# Checking Status for Student 1
print("Status for student1:", status1)

student2 = Student('Jenny', 69)  # Instantiate student2 object
status2 = student2.passOrFail()  # Call passOrFail method for student2

# Checking Status for Student 2
print("Status for student2:", status2)

# Replacing passing criteria from 50 to 60 by updating passingMark variable using class
Student.passingMark = 60

# Call passOrFail method for student1 and student2 again
status1 = student1.passOrFail()
status2 = student2.passOrFail()

# Print the updated statuses of both Students, Student 1 will Fail because passing marks are 60 
print("Updated status for student1:", status1)
print("Updated status for student2:", status2)
