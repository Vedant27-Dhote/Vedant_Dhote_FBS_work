'''Implement a generator function that yields palindrome numbers.
Palindromes are numbers that read the same backward as forward
(e.g., 121, 1331). Generate palindromes lazily and infinitely.'''

def palindrome():
    number = 0

    while True:
        if str(number) == str(number)[::-1]:
            yield number

        number += 1


p = palindrome()

for i in range(10):
    print(next(p))