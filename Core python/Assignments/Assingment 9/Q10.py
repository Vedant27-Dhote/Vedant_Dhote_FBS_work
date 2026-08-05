def reverse_str_recursion(n):
    if len(str(n)) == 1:
        return str(n)
    return str(n)[-1] + reverse_str_recursion(str(n)[:-1])

num = 9876
reversed_num = int(reverse_str_recursion(num))
print("Original:", num)
print("Reversed:", reversed_num)
