# Input 5 subject marks from user and display grade(eg.First class,Second class ..)


print("Enter marks for 5 subjects (out of 100):")
sub1 = float(input("Subject 1: "))
sub2 = float(input("Subject 2: "))
sub3 = float(input("Subject 3: "))
sub4 = float(input("Subject 4: "))
sub5 = float(input("Subject 5: "))


total_marks = sub1 + sub2 + sub3 + sub4 + sub5
average = total_marks / 5

print(f"\nTotal Marks: {total_marks} / 500")
print(f"Percentage: {average}%")


if average >= 75:
    print("Grade: Distinction")
elif average >= 60:
    print("Grade: First Class")
elif average >= 50:
    print("Grade: Second Class")
elif average >= 35:
    print("Grade: Pass Class")
else:
    print("Grade: Fail")
