'''WAP to print Armstrong number within a given range'''
lower = int(input("Enter lower bound of range: "))
upper = int(input("Enter upper bound of range: "))


for num in range(lower, upper + 1):
    
    num_str = str(num)
    num_digits = len(num_str)
    
    total_sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total_sum += digit ** num_digits
        temp //= 10
        

    if num == total_sum:
        print(num)
