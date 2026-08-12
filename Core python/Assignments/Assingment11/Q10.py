
def remove_even_numbers(original_list):
    only_odds = []
    
    for num in original_list:

        if num % 2 != 0:
            only_odds.append(num)
            
    return only_odds


my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_even_numbers(my_numbers)
print("List with only odd numbers:", result)
