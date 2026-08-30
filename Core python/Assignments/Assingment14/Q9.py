def three_sum(numbers, target):
    numbers.sort()
    triplets = []
    
    for i in range(len(numbers) - 2):
        if i > 0 and numbers[i] == numbers[i-1]:
            continue
            
        left = i + 1
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[i] + numbers[left] + numbers[right]
            
            if current_sum == target:
                triplets.append([numbers[i], numbers[left], numbers[right]])
                while left < right and numbers[left] == numbers[left+1]:
                    left += 1
                while left < right and numbers[right] == numbers[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
    return triplets

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums, 0))  
