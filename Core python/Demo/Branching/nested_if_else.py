gender = input("Enter gender (m/f):")
age = int(input("Enter age:"))

if(gender=='f'):
    if(age>=18):
        print("The girl is eligible for marragie")
    else:
        print("girl is not eligible for marragie")
else:
    if(age>=21):
        print("The boy is eligible for marraige")
    else:
        print("the boy is eligible for marriage")