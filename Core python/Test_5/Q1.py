'''A list contains the denominations as follows :
D = [2000, 500, 200, 100 , 50, 20, 10, 5]
Accept an amount from user and calculate how many
minimum number of notes will be needed for that
amount.'''

D = [2000, 500, 200, 100, 50, 20, 10, 5]

amount = int(input("Enter the amount: "))

total_notes = 0

for note in D:
    if amount >= note:
        count = amount // note      
        amount = amount % note      
        total_notes = total_notes + count
        print(f"{note}:{count}")

print("Total minimum notes needed:", total_notes)
