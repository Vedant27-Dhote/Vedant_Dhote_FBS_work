def get_cubes(numbers):
    cubes_list = []
    for num in numbers:
        cube = num * num * num
        cubes_list = cubes_list + [cube]
    return cubes_list

list = [10,20,20,30,40,50,50]
res = get_cubes(list)
print(res)
