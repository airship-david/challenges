#
# David Engel
#
# Challenge: Parking Lot
#
# Instructions:
# - Design a parking lot using object-oriented principles.
#
# Goals:
# - Your solution should be in Python 3
#
# Assumptions:
# - The parking lot can hold motorcycles, cars and vans
# - The parking lot has compact spots, regular spots and large spots
# - A motorcycle can park in any spot
# - A car can park in a single compact spot, or a regular spot
# - A van can park in a large spot or 3 regular spots
#
# Here are a few methods that you should be able to run:
# - Tell us how many spots are remaining
# - Tell us how many total spots are in the parking lot
# - Tell us when the parking lot is full
# - Tell us when the parking lot is empty
# - Tell us when certain spots are full e.g. when all motorcycle spots are taken
# - Tell us how many spots vans are taking up
#

import random
import time

# Parent Vehicle
class Vehicle:
    def __init__(self):
        self.type = 'vehicle'
        self.allowed_parking_spots = {
            'compact': 1,
            'regular': 1,
            'large': 1
        }
        self.location = ''

    def spot(self, location: str):
        self.location = location

# Motorcycle
class Motorcycle(Vehicle):
    def __init__(self):
        self.type = 'motorcycle'
        self.allowed_parking_spots = {
            'compact': 1,
            'regular': 1,
            'large': 1
        }

# Car
class Car(Vehicle):
    def __init__(self):
        self.type = 'car'
        self.allowed_parking_spots = {
            'regular': 1,
            'compact': 1
        }

# Van
class Van(Vehicle):
    def __init__(self):
        self.type = 'van'
        self.allowed_parking_spots = {
            'large': 1,
            'regular': 3
        }

# Parking Lot
class ParkingLot:
    def __init__(self, compact_spots: int, regular_spots: int, large_spots: int):
        self.total = {
            'compact': compact_spots,
            'regular': regular_spots,
            'large': large_spots
        }

        self.available = {
            'compact': compact_spots,
            'regular': regular_spots,
            'large': large_spots
        }

        self.parked = {
            'motorcycle': 0,
            'car': 0,
            'van': 0
        }

    # Park a vehicle
    def park(self, vehicle):
        for spot in vehicle.allowed_parking_spots.keys():
            if self.available[spot] >= vehicle.allowed_parking_spots[spot]:
                self.available[spot] -= vehicle.allowed_parking_spots[spot]
                self.parked[vehicle.type] += 1
                vehicle.spot(spot)
                print('Parked in ' + str(vehicle.allowed_parking_spots[spot]) + ' ' + spot + (' spot.' if vehicle.allowed_parking_spots[spot] == 1 else ' spots.'))
                return
            else:
                print(spot.capitalize()+' spots full!')

        print('Parking lot is full for ' + vehicle.type + 's!')

    # Display total parking spots
    def total_spots(self):
        total = 0
        for type in self.total.keys():
            total += self.total[type]

        print('\nTotal Spots: ' + str(total))
        for type in self.total.keys():
            print(' - ' + type.capitalize() + ' Spots: ' + str(self.total[type]))

    # Display remaining parking spots
    def remaining_spots(self):
        available = 0
        for type in self.available.keys():
            available += self.available[type]

        print('\nRemaining Spots: ' + str(available))
        for type in self.available.keys():
            print(' - ' + type.capitalize() + ' Spots: ' + str(self.available[type]))

    # Display parked vehicles
    def parked_stats(self):
        for type in self.parked.keys():
            print(type.capitalize() + 's Parked: ' + str(self.parked[type]))

    # Parking lot status
    def status(self):
        total = 0
        for type in self.total.keys():
            total += self.total[type]

        available = 0
        for type in self.available.keys():
            available += self.available[type]

        if available == total:
            print('\nStatus: Parking lot is empty!')
        elif available == 0:
            print('\nStatus: Parking lot is full!')
        else:
            print('\nStatus: Parking lot has available spots!')

    # Parking lot availability
    def availability(self):
        available = 0
        for type in self.available.keys():
            available += self.available[type]

        if available == 0:
            return False
        else:
            return True

# Play the funky music...
if __name__ == '__main__':
    # Welcome
    print('Welcome to David Engel\'s Parking Lot!\n')

    # How many parking spots do we have?
    compact_spots = int(input('Enter # of compact parking spots: '))
    regular_spots = int(input('Enter # of regular parking spots: '))
    large_spots = int(input('Enter # of large parking spots: '))

    # Set up the lot
    lot = ParkingLot(compact_spots, regular_spots, large_spots)
    lot.status()
    lot.total_spots()
    lot.parked_stats()

    # Accept vehicles until full
    while lot.availability():
        # Generate random vehicle type
        r = random.randint(1, 3)
        if r == 1:
            vehicle = Motorcycle()
        elif r == 2:
            vehicle = Car()
        elif r == 3:
            vehicle = Van()

        # Park vehicle
        print('\nParking ' + vehicle.type + '...')
        lot.park(vehicle)

        # Pause to simulate time passing between vehicles
        t = random.random()
        time.sleep(t)

    # Print result
    lot.status()
    lot.remaining_spots()
    lot.parked_stats()