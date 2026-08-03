'''Accept no. of passengers from user and per ticket cost. Then accept age of each
passenger and then calculate total amount to ticket to travel for all of them based on
following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.'''

passanger = int(input("Enter the number of passanger:"))
cost = int(input("Enter the cost of Ticket:"))

for i in range(passanger):
    print("passanger no",i+1)
    final_cost = 0
    age = int(input("Enter the age of passanger:"))
    if age<12:
        final_cost = cost -(cost*30)/100
        print(f"The final cost to travel for you is: {final_cost}")
    elif age>59:
        final_cost = cost - (cost*50)/100
        print(f"The final cost to travel for you is: {final_cost}")
    else:
        print(f"The final cost to travel for you is: {cost}")

