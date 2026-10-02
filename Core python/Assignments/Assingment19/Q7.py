'''Use a nested list comprehension to find all of the numbers from
1–1000 that are divisible by any single digit.'''


numbers = [n for n in range(1, 1001) for digit in range(2, 10) if n % digit == 0]
print("Numbers divisible by any single digit:", numbers)

