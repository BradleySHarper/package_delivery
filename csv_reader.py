# Author: Bradley Harper
# Student ID: 001547272
# C950 Data Structures & Algorithms II

import csv
import hashmap
import package


# Function that takes in file name and hash table, inserts into hash table
def load_package_data(file_name, hash_table):
    with open(file_name) as packages:
        package_data = csv.reader(packages, delimiter=',')
        for row in package_data:
            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            delivery = row[5]
            size = row[6]
            note = row[7]

            p = package.Package(package_id, address, city, state, zip, delivery, size,
                                note)

            # inserts package into the hash table
            hash_table.insert(package_id, p)


new_hash = hashmap.ChainingHashTable()
load_package_data('package_data.csv', new_hash)
