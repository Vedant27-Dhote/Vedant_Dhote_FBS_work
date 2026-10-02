'''Write a program to accept basic salary of n emp. (n should be
accepted from user). If basic salary is below 20000 then
da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and
hra=20%. Based on this calculate the total salary of each emp
and also total salary of all emp.'''

n = int(input("Enter the number of employees: "))
total_salary = 0

for i in range(n):
    basic_salary = float(input(f"Enter the basic salary of employee {i + 1}: "))
    
    if basic_salary < 20000:
        da = 0.10 * basic_salary
        ta = 0.12 * basic_salary
        hra = 0.15 * basic_salary
    else:
        da = 0.15 * basic_salary
        ta = 0.18 * basic_salary
        hra = 0.20 * basic_salary

    total_emp_salary = basic_salary + da + ta + hra
    total_salary += total_emp_salary

print(f"Total salary of all employees: {total_salary}")