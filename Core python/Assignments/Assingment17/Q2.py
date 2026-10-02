'''Create a derived class from Student as EnggStudent with :
a. Data members as :
i. Branch
ii. InternalMarks
b. Add the following methods :
i. Parameterized constructor
ii. Display
iii. Accept
iv. override Method CalculateRank
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
        if self.percentage >= 90: return "Rank 1"
        elif self.percentage >= 75: return "Rank 2"
        elif self.percentage >= 50: return "Rank 3"
        else: return "Pass/Fail"

    def Display(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Percentage: {self.percentage}%")

    def __str__(self):
        return f"Student: {self.name}"


class EnggStudent(Student):

    def __init__(self, student_id=0, name="Unknown", age=0, percentage=0.0, branch="General", internal_marks=0):
        super().__init__(student_id, name, age, percentage)
        self.branch = branch
        self.internal_marks = internal_marks


    def Accept(self):
        super().Accept()  
        self.branch = input("Enter Branch (e.g., Computer, Mechanical): ")
        self.internal_marks = int(input("Enter Internal Marks (out of 50): "))

    def CalculateRank(self):

        total_score = self.percentage + (self.internal_marks * 2) 
        
        if total_score >= 150:
            return "Elite Engineer (Distinction)"
        elif total_score >= 120:
            return "First Class Engineer"
        elif total_score >= 90:
            return "Second Class Engineer"
        else:
            return "Pass"

    def Display(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Branch: {self.branch} | Internal Marks: {self.internal_marks} | Rank: {self.CalculateRank()}")

    def __str__(self):
        return f"EnggStudent :- [Name: {self.name}, Branch: {self.branch}]"


engg1 = EnggStudent(201, "Amit", 21, 82.0, "Computer Science", 45)

engg1.Display()
print(engg1)  

engg2 = EnggStudent()
engg2.Accept()

engg2.Display()

    
