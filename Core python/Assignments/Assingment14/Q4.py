def find_pairs_with_sum(numbers, target):
    seen = set()
    pairs = set()  
    
    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
        
    return list(pairs)

nums = [1, 2, 3, 4, 5, 2]
print(find_pairs_with_sum(nums, 5))  
