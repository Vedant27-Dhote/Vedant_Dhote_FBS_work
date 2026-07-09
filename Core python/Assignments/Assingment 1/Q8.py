#Write a program to convert days into years, weeks and days.
day = int(input("Enter the Days:-"))

year = int((day/365))
weeks = int((day - (year*365))/7)
days = int(day-((year*365)+(weeks*7)))
print(year)
print(weeks)
print(days)