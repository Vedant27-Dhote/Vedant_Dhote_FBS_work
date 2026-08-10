def generate_powers(numbers):
    squares = []
    cubes = []

    for num in numbers:
        squares = squares + [num * num]
        cubes = cubes + [num * num * num]
        
    return numbers, squares, cubes

list = [1,2,3,4,5,6,7,8]
res = generate_powers(list)
print(res)