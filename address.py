# Author: Bradley Harper
# Student ID: 001547272
# C950 Data Structures & Algorithms II

import csv

# Creates a list to hold addresses
address_list = []


# Address retrieval function
def load_address_data(file_name):
    with open(file_name) as addresses:
        reader = csv.reader(addresses, delimiter=',')
        for row in reader:
            address_list.append(row)


# Loads address data from csv file
load_address_data('distance_name_data.csv')


# Function that finds address and returns address ID
def get_address(address):
    for row in address_list:
        if address in row[2]:
            return int(row[0])
