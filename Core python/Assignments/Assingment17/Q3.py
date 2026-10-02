class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def Accept(self):
        self.roll_no = int(input("Enter Roll No: "))
        self.name = input("Enter Name: ")
        self.marks = float(input("Enter Marks: "))

    def CalculateRank(self):
        if self.marks >= 75:
            return "Distinction"
        elif self.marks >= 60:
            return "First Class"
        elif self.marks >= 50:
            return "Second Class"
        else:
            return "Pass"

    def Display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Rank:", self.CalculateRank())

    def __str__(self):
        return f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}"


class MedicalStudent(Student):

    def __init__(self, roll_no, name, marks, specialization, marks_of_internship):
        super().__init__(roll_no, name, marks)
        self.specialization = specialization
        self.marks_of_internship = marks_of_internship

    def Accept(self):
        super().Accept()
        self.specialization = input("Enter Specialization: ")
        self.marks_of_internship = float(input("Enter Marks of Internship: "))

    def CalculateRank(self):
        total_marks = self.marks + self.marks_of_internship

        if total_marks >= 150:
            return "Distinction"
        elif total_marks >= 120:
            return "First Class"
        elif total_marks >= 100:
            return "Second Class"
        else:
            return "Pass"

    def Display(self):
        super().Display()
        print("Specialization:", self.specialization)
        print("Marks of Internship:", self.marks_of_internship)

    def __str__(self):
        return (f"Roll No: {self.roll_no}, Name: {self.name}, "
                f"Marks: {self.marks}, Specialization: {self.specialization}, "
                f"Internship Marks: {self.marks_of_internship}")


m = MedicalStudent(101, "Vedant", 80, "Cardiology", 75)

print(m)
m.Display()
print("Rank:", m.CalculateRank())