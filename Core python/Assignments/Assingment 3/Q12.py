#Write a program to check if given 3 digit number is a palindrome or not.



num = int(input("Enter a 3-digit number: "))


digit1 = num // 100          
digit2 = (num // 10) % 10    
digit3 = num % 10            


reversed_num = (digit3 * 100) + (digit2 * 10) + digit1




if num == reversed_num:
    print(f"Yes, {num} is a Palindrome number.")
else:
    print(f"No, {num} is not a Palindrome number.")

