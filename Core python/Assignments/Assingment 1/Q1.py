# Write a program to calculate the percentage of student based on marks of any 5 subjects.
sub1 = float(input("Enter the marks of Subject1:-"))
sub2 = float(input("Enter the marks of Subject2:-"))
sub3 = float(input("Enter the marks of Subject3:-"))
sub4 = float(input("Enter the marks of Subject4:-"))
sub5 = float(input("Enter the marks of Subject5:-"))

Obtained_Marks = sub1+sub2+sub3+sub4+sub5
Total_Marks = 500
percentage = (Obtained_Marks/Total_Marks) * 100 #formula of percentage
print(f"You got {percentage}% in the Examination")
