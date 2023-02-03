# Author: Bradley Harper
# Student ID: 001547272
# C950 Data Structures & Algorithms II

# Package class for creating package objects
class Package:
    def __init__(self, ID, address, city, state, zip, deadline, mass, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.status = None
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.ID, self.address, self.city, self.state, self.zip, self.deadline, self.mass, self.delivery_time,
            self.status)

# Function for changing package status based on time argument
    def status_change(self, time):
        if self.delivery_time < time:
            self.status = "Delivered"
        elif self.departure_time < time:
            self.status = "En route"
        else:
            self.status = "At Hub"

