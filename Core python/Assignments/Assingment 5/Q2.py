'''Enter number of students from user. For those many students accept marks of 5
subject marks from user and calculate percentage. Display all percentage and
average percentage of students.'''



num_students = int(input("Enter number of students: "))


total_percentage_sum = 0

for i in range(1, num_students + 1):
    print(f"\n--- Enter marks for Student {i} ---")
    student_marks_sum = 0
    
    
    for j in range(1, 6):
        mark = float(input(f"Enter marks for Subject {j}: "))
        student_marks_sum += mark
        
    percentage = (student_marks_sum / 500) * 100
    total_percentage_sum += percentage
    
    
    print(f"Student {i} Percentage: {percentage:.2f}%")


average_percentage = total_percentage_sum / num_students
print(f"\n=== Final Class Average ===")
print(f"Average Percentage of all students: {average_percentage:.2f}%")
