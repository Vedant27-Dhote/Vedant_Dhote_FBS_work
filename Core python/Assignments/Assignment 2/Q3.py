#Q. Convert distant given in feet and inches into meter and centimeter.
Feet = float(input("Enter the distance in feet:-"))
inches = float(input("Entre the distance in inches:-"))

Total_inches = Feet*12 + inches

Total_cm = Total_inches* 2.54

M = Total_cm // 100
cm = Total_cm - M*100

print(f"The distance is {M}metre and {cm}centimetere")

