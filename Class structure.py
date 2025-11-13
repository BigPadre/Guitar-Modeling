# Define a class
class Bike:
    # Class attributes
    name = ""
    gear = 0

    # Method to display bike details
    def display_details(self):
        print(f"Bike Name: {self.name}, Gears: {self.gear}")

# Create an object of the class
bike1 = Bike()

# Assign values to attributes
bike1.name = "Mountain Bike"
bike1.gear = 21

# Call the method
bike1.display_details()