'''Accept age of five people and also per person ticket amount and then calculate total
amount to ticket to travel for all of them based on following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.'''


base_price = float(input("Enter the per person ticket amount: "))


total_amount = 0.0


print("\nEnter the ages of the 5 people:")
for i in range(1, 6):
    age = int(input(f"Person {i} age: "))
    
    
    if age < 12:
        ticket_price = base_price * 0.70
        
    
    elif age > 59:
        ticket_price = base_price * 0.50
        
    
    else:
        ticket_price = base_price
        
    
    total_amount += ticket_price


print(f"\nThe total ticket amount for all 5 people is: {total_amount:.2f}")
