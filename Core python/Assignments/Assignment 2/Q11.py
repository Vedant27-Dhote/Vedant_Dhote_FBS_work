#Q. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

Amt = 17388

Five_hundred_notes = Amt // 500
Two_Hundred_notes = (Amt - (Five_hundred_notes*500)) // 200
Hundred_notes = (Amt-(Five_hundred_notes*500+Two_Hundred_notes*200))//100
Fifty_notes = (Amt-(Five_hundred_notes*500+Two_Hundred_notes*200+Hundred_notes*100))//50
twenty_notes = (Amt-(Five_hundred_notes*500+Two_Hundred_notes*200+Hundred_notes*100+Fifty_notes*50))//20
Ten_notes = (Amt-(Five_hundred_notes*500+Two_Hundred_notes*200+Hundred_notes*100+Fifty_notes*50+twenty_notes*20))//10
Coin_5 = (Amt -(Five_hundred_notes*500+Two_Hundred_notes*200+Hundred_notes*100+Fifty_notes*50+twenty_notes*20+Ten_notes*10))//5
Coin_2 = (Amt-(Five_hundred_notes*500+Two_Hundred_notes*200+Hundred_notes*100+Fifty_notes*50+twenty_notes*20+Ten_notes*10+Coin_5*5))//2
Coin_1 = (Amt-(Five_hundred_notes*500+Two_Hundred_notes*200+Hundred_notes*100+Fifty_notes*50+twenty_notes*20+Ten_notes*10+Coin_5*5+Coin_2*2))//1

print("For Above Amount you requires:-")
print(f"number of 500rs notes:-{Five_hundred_notes}")
print(f"number of 200rs notes:-{Two_Hundred_notes}")
print(f"number of 100rs notes:-{Hundred_notes}")
print(f"number of 50rs notes:-{Fifty_notes}")
print(f"number of 20rs notes:-{twenty_notes}")
print(f"number of 10rs notes:-{Ten_notes}")
print(f"number of 5 coin:-{Coin_5}")
print(f"number of 2 coin:-{Coin_2}")
print(f"number of 1 coin:-{Coin_1}")

