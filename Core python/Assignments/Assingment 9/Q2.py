def armstrong_sum(num, power):
    if num == 0:
        return 0
    digit = num % 10
    return (digit ** power) + armstrong_sum(num // 10, power)

def is_armstrong(num):
    power = len(str(num))
    return num == armstrong_sum(num, power)

number = 153  
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is NOT an Armstrong number.")
