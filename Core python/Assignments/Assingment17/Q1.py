'''Create a class Student with following
a. data members :
i. StudentId
ii. Name
iii. Age
iv. Percentage
b. Add the following methods :
i. Parameterized constructor
ii. Display
iii. Accept
iv. Method CalculateRank
v. Override __str__ Method'''

class Student:
    def __init__(self, student_id=0, name="Unknown", age=0, percentage=0.0):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = percentage

    
    def Accept(self):
        self.student_id = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    
    def CalculateRank(self):
        if self.percentage >= 90:
            return "Rank 1 (Excellent)"
        elif self.percentage >= 75:
            return "Rank 2 (Very Good)"
        elif self.percentage >= 50:
            return "Rank 3 (Good)"
        elif self.percentage >= 35:
            return "Pass"
        else:
            return "Fail"

    
    def Display(self):
        print(f"ID: {self.student_id}   Name: {self.name}   Age: {self.age}   Percentage: {self.percentage}%   Rank: {self.CalculateRank()}")


    def __str__(self):
        return f"Student:- [ID: {self.student_id}, Name: {self.name}]"



student1 = Student(101, "Rahul", 20, 88.5)
student1.Display()

print(student1)  

student2 = Student()  
student2.Accept()     
student2.Display()
