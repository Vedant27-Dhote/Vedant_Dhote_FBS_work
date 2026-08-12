def print_snakes_and_ladders():
    current_number = 100
    left_to_right = False
    
    for row in range(10):
        row_numbers = []
        
        for col in range(10):
            row_numbers.append(current_number)
            current_number = current_number - 1
            
        if left_to_right == True:
            row_numbers.reverse()
            
        for num in row_numbers:
            print(num, end="\t")
        print() 
        
        left_to_right = not left_to_right


print_snakes_and_ladders()
