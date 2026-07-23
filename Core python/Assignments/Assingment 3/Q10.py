# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)


gender = input("Enter gender (Male/Female): ")
age = int(input("Enter age: "))

if gender == "male":
    if age >= 21:
        print(" Eligible to marry.")
    else:
        print("not Eligible")

elif gender == "female":
    if age >= 18:
        print(" Eligible to marry.")
    else:
        print("Not eligible")

else:
    print("\n Invalid gender input. Please enter 'Male' or 'Female'.")

