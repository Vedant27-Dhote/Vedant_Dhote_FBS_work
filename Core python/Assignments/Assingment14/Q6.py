def max_product_pair(numbers):
    unique_nums = sorted(list(set(numbers)))
    
    if len(unique_nums) < 2:
        return None
    
    prod1 = unique_nums[-1] * unique_nums[-2]
    prod2 = unique_nums[0] * unique_nums[1]
    
    if prod1 > prod2:
        return unique_nums[-2], unique_nums[-1]
    else:
        return unique_nums[0], unique_nums[1]


nums = [-10, -5, 1, 2, 3, 4]
print(max_product_pair(nums)) 
