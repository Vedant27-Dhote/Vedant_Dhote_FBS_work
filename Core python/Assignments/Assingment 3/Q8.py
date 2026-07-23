# Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise
#failed. (Something like captcha)                                                                                                                                                       



import random
CORRECT_USERID = "admin"
CORRECT_PASSWORD = "password123"


entered_userid = input("Enter User ID: ")
entered_password = input("Enter Password: ")


if entered_userid == CORRECT_USERID and entered_password == CORRECT_PASSWORD:
    print("\nLogin credentials verified successfully!")
    
    
    captcha_code = random.randint(1000, 9999)
    print(f"Your 4-digit verification code is: {captcha_code}")
    
    
    user_captcha = input("Enter the verification code shown above: ")
    
    
    if user_captcha == str(captcha_code):
        print("\nSuccess: Verification complete!")
    else:
        print("\nFailed: Incorrect verification code.")
        
else:
    print("\nFailed: Invalid User ID or Password.")
