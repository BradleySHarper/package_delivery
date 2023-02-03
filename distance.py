# Author: Bradley Harper
# Student ID: 001547272
# C950 Data Structures & Algorithms II

import csv

# Creates list to hold distances
distance_list = []


# Distance retrieval function
def load_distance_data(file_name):
    with open(file_name) as distances:
        reader = csv.reader(distances, delimiter=',')
        for item in reader:
            distance_list.append(item)
        return distance_list


# Function that finds distances based on 2 address arguments and returns distance
# Utilizes Value Error exception to return inverse data if argument location is blank
def get_distance(address1, address2):
    try:
        return float(load_distance_data('distance_data.csv')[address1][address2])
    except ValueError:
        return float(load_distance_data('distance_data.csv')[address2][address1])
