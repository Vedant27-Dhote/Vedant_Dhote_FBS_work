def remove_even_numbers(numbers):
    only_odds = []
    for num in numbers:
        if num % 2 != 0:
            only_odds = only_odds + [num]
    return only_odds

list = [1,2,3,4,5,6,7,8,9]
res = remove_even_numbers(list)
print(list)
