n = int(input("Enter the number:"))

if n<0:
    print("The number is negative")
else:
    if n> 0 and n<50:
        print("Number lies between 0 to 50")
    else:
        if n>50 and n<100:
            print("Number lies between 50 to 100")
        else:
            if n>100 and n<150:
                print("Number lies between 100 to 150")
            else:
                if n>150 and n<250:
                    print("Number lies between 150 to 250")
                else:
                    print("Number is greater than 250")
        