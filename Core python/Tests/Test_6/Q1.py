'''Write a program which calculates toll calculation on some location following
is data provided:
Many vehicles goes through the toll every vehicle has to pay the basic
toll + extra charges if any.
two wheelers have to pay basic toll Rs 20 three wheelers have to pay
30 and four wheelers have to pay 40
heavy veheicles i.e. Vehicles having wheels more than four, have to
pay 60 Rs as basic toll
extra charges :
for two wheelers if no. of persons are more than two extra charge
=10/person
for three wheelers if no. of persons are more than 3 extra charge
=20/person
for four wheelers if no. of persons are more than 4 extra charge
=40/person
for heavy vehicle if no. of person are more than 6 extra charges
=100/person.
Show polymorphic behaviour in main. Main module should be
designed in such way that toll should easily operate it through
interactive menu driven program .
Object of vehicle class should not be possible.'''

from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, wheels, persons):
        self.wheels = wheels
        self.persons = persons

    @abstractmethod
    def calculate_toll(self):
        pass


class TwoWheeler(Vehicle):

    def calculate_toll(self):
        toll = 20

        if self.persons > 2:
            extra_persons = self.persons - 2
            toll += extra_persons * 10

        return toll


class ThreeWheeler(Vehicle):

    def calculate_toll(self):
        toll = 30

        if self.persons > 3:
            extra_persons = self.persons - 3
            toll += extra_persons * 20

        return toll


class FourWheeler(Vehicle):

    def calculate_toll(self):
        toll = 40

        if self.persons > 4:
            extra_persons = self.persons - 4
            toll += extra_persons * 40

        return toll


class HeavyVehicle(Vehicle):

    def calculate_toll(self):
        toll = 60

        if self.persons > 6:
            extra_persons = self.persons - 6
            toll += extra_persons * 100

        return toll


def main():

    while True:

        print("\n========== TOLL PLAZA ==========")
        print("1. Two Wheeler")
        print("2. Three Wheeler")
        print("3. Four Wheeler")
        print("4. Heavy Vehicle")
        print("5. Exit")
        print("================================")

        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Thank you!")
            break

        persons = int(input("Enter number of persons: "))

        if choice == 1:
            vehicle = TwoWheeler(2, persons)

        elif choice == 2:
            vehicle = ThreeWheeler(3, persons)

        elif choice == 3:
            vehicle = FourWheeler(4, persons)

        elif choice == 4:
            wheels = int(input("Enter number of wheels: "))
            vehicle = HeavyVehicle(wheels, persons)

        else:
            print("Invalid choice")
            continue

        print("Total Toll = Rs.", vehicle.calculate_toll())


main()