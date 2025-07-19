# abstrcation is basically use tp hiding unnecesay details from users through class and methods.

class Student:
    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage
        
    def student_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.percentage} %")
        
student1 = Student('Debojit',12,90)
student2 = Student('Krishna',12,97)

# print(student1.student_details)
# print(student1.__dict__)

student1.student_details()

# def student_details(self):
#         print(f"{self.name} is in class {self.grade}, with {self.percentage} %")
        # it is an esample of abstraction in which we are hiding the some data from the user..
        