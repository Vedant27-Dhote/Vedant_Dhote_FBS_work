#Write a program to check if user has entered correct userid and password.
user_id = input("Enter user id:-")
password = input("Enter password:-")

saved_id = 'user@99'
saved_pass = 'PASS@123'

if user_id == saved_id and password == saved_pass:
    print("You have entered right id and password")

else:
    print("Wrong id or password try again")
