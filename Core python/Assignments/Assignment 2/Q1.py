# Q.Convert the time entered in hh,min and sec into seconds.
H = int(input("Enter hours:-"))
M = int(input("Enter miniutes:-"))
S = int(input("Enter seconds:-"))

Total = H*60*60 + M*60 + S
print(f"The total Seconds are:-{Total}")
