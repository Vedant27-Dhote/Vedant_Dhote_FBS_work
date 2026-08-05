def reverse_number(num, rev=0):
    if num == 0:
        return rev
    last_digit = num % 10
    return reverse_number(num // 10, rev * 10 + last_digit)

original_num = 12345
print("Original:", original_num)
print("Reversed:", reverse_number(original_num))
