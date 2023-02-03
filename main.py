# Author: Bradley Harper
# Student ID: 001547272
# C950 Data Structures & Algorithms II

import truck
import package
import datetime

# instance of Truck number 1
truck_1_packages = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 39, 40]
truck_1 = truck.Truck(truck_1_packages, 0.0, "4001 South 700 East",
                      datetime.timedelta(hours=8))

# instance of Truck number 2
truck_2_packages = [3, 5, 6, 18, 25, 26, 28, 32, 36, 38]
truck_2 = truck.Truck(truck_2_packages, 0.0,
                      "4001 South 700 East", datetime.timedelta(hours=9, minutes=10))

# instance of Truck number 3
truck_3_packages = [2, 4, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 27, 33, 35]
truck_3 = truck.Truck(truck_3_packages, 0.0, "4001 South 700 East",
                      datetime.timedelta(hours=10, minutes=20))

# Deliver packages on all trucks
truck.package_delivery(truck_1)
truck.package_delivery(truck_2)
truck.package_delivery(truck_3)

# User Interface below
print("Welcome to WGUPS!")
print("*****************")
print(
    "Total distance driven by all trucks: " + str(float("{:.2f}".format(truck_1.miles + truck_2.miles + truck_3.miles)))
    + " miles")
print("*****************")
print("Please choose an option below (Enter a 1 or 2)")
print("1. Search for a package by ID number.")
print("2. Display all packages.")

# Provides user with option to see all packages or a single package
user_choice = input("Enter a 1 or 2 to continue: ")

# Prompts user to enter a single package ID and time to view package status
if user_choice == "1":
    package_input = input("Enter a package ID number to proceed: ")
    try:
        time_input = input("Enter a time to display package status using the format hh:mm:ss ")
        (h, m, s) = time_input.split(":")
        delta_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        packages = truck.hash_data_structure.search(int(package_input))
    except ValueError:
        print("Invalid Input, Closing Program")
        exit()
    print("-----------------------------------------------")
    print("Packages are displayed in the following format:")
    print("Package ID, Address, City, State, ZIP code, Delivery Deadline, Weight, Time Delivered, Status")
    print("-----------------------------------------------")
    # Updates package 9 address, dependent on time chosen by user
    if package_input == "9":
        if delta_time < datetime.timedelta(hours=10, minutes=20):
            package.address = "300 State St"
            package.zip = "84103"
    # Updates package status dependent on time chosen by user
    packages.status_change(delta_time)
    print(packages)

# Prompts user to enter a time to view all package statuses at the chosen time
elif user_choice == "2":
    try:
        time_input = input("Enter a time to display all package status using the format hh:mm:ss ")
        (h, m, s) = time_input.split(":")
        delta_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    except ValueError:
        print("Invalid Input, Closing Program")
        exit()
    print("-----------------------------------------------")
    print("Packages are displayed in the following format:")
    print("Package ID, Address, City, State, ZIP code, Delivery Deadline, Weight, Status, Time Delivered")
    print("-----------------------------------------------")
    # Loops through all packages and prints status at user given time
    for package_ID in range(1, 41):
        package = truck.hash_data_structure.search(package_ID)
        if package_ID == 9:
            if delta_time < datetime.timedelta(hours=10, minutes=20):
                package.address = "300 State St"
                package.zip = "84103"
        package.status_change(delta_time)
        if package.status == "Delivered":
            print(package_ID,
                  str("= " + package.address + ", " + package.city + ", " + package.state + ", " + package.zip +
                      ", " + package.deadline + ", " + package.mass + ", " + package.status + " at"), +
                  package.delivery_time)
        else:
            print(package_ID,
                  str("= " + package.address + ", " + package.city + ", " + package.state + ", " + package.zip +
                      ", " + package.deadline + ", " + package.mass + ", " + package.status))

else:
    print("Invalid Input, Closing Program")
    exit()
