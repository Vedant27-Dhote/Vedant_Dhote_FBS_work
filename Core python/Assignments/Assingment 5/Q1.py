'''Write a program to prompt user to enter userid and password. If Id and
password is incorrect give him chance to re-enter the credentials. Let him try 3
times. After that program to terminate.'''

org_id = "vedant@99"
org_pass = "12345"

for i in range(3):

    Id = input("Enter user id:")
    password = input("Enter password")
    if Id == org_id and password==org_pass:
        print("Welcome user:")
    else:
        print("Wrong credentials Try again:-")
else:
    print("You are out of attempt")

