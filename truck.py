# Author: Bradley Harper
# Student ID: 001547272
# C950 Data Structures & Algorithms II

import datetime
import address
import csv_reader
import distance
import hashmap


# Truck class for creating truck objects
class Truck:
    def __init__(self, packages, miles, address, depart_time):
        self.packages = packages
        self.miles = miles
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time

    def __str__(self):
        return "%s, %s, %s, %s" % (self.packages, self.miles,
                                   self.address, self.depart_time)


# Creates an instance of a Chaining Hash Table
hash_data_structure = hashmap.ChainingHashTable()

# Loads packages into the hash table
csv_reader.load_package_data('package_data.csv', hash_data_structure)


# Function that delivers packages utilizing the nearest neighbor algorithm
# Takes a truck object argument
# Updates truck mileage and individual package delivery times
def package_delivery(truck):
    # Empty list for packages on truck to be placed
    packages_on_truck = []

    # Places all packages on truck into list, utilizing instance of hash table above
    for package_Id in truck.packages:
        loaded_package = hash_data_structure.search(package_Id)
        packages_on_truck.append(loaded_package)

    # Empties the truck's package list
    # truck.packages = []

    # Loops through packages_on_truck list, finding the nearest package delivery address
    while len(packages_on_truck) > 0:
        package_to_deliver = None
        delivery_address = 50
        for package in packages_on_truck:
            if distance.get_distance(address.get_address(truck.address),
                                     address.get_address(package.address)) <= delivery_address:
                delivery_address = distance.get_distance(address.get_address(truck.address),
                                                         address.get_address(package.address))
                package_to_deliver = package

        # Changes package depart time to truck depart time
        package_to_deliver.departure_time = truck.depart_time
        # Removes that package from the packages on truck
        packages_on_truck.remove(package_to_deliver)
        # Changes truck's address to the package's address
        truck.address = package_to_deliver.address
        # Calculates time traveled and adds to the truck time
        # Divides by 18 since the universal speed of the trucks is 18 mph
        truck.time += datetime.timedelta(hours=delivery_address / 18)
        # Changes delivery time of package to the current truck time above
        package_to_deliver.delivery_time = truck.time
        # Adds the distance traveled to the truck mileage
        truck.miles += delivery_address
        # Appends package with the nearest address back in truck.packages list, completing delivery
        truck.packages.append(package_to_deliver.ID)


# Function to return hash table
def hashing():
    return hash_data_structure
