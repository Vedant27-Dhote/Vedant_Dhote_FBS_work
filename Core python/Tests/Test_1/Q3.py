'''Write a program to accept distance in km and convert it into meters and
centimeters both.'''
distance_km = float(input("Enter the distance in kilometers: "))
distance_meters = distance_km * 1000
distance_centimeters = distance_km * 100000
print("Distance in meters:", distance_meters)
print("Distance in centimeters:", distance_centimeters)