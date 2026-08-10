'''Accept a number from user and check if this element is present in the list or
not. Also tell how many times it is present in the list.'''
def check_and_count(numbers, target):
    count = 0
    present = False

    for num in numbers:
        if num == target:
            present = True
            count += 1

    if present:
        print(f"{target} is present {count} times.")
    else:
        print(f"{target} is not present in the list.")

list = [10,20,30,45,67,86]
target = int(input("Enter the number to search in the list:"))
check_and_count(list,target)