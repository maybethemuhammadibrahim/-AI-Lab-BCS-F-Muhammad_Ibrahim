
class Vehicle:
    def __init__(self, vehicle_id, brand, rent_perday):
        self.vehicle_id =vehicle_id
        self.brand =brand
        self.rent_perday=rent_perday

    def display_details(self):
        print("Vehicle ID:", self.vehicle_id)
        print("Brand:", self.brand)
        print("Rent per day:", self.rent_perday)

    def calculate_rent(self, days):
        total = self.rent_perday * days
        return total


car1 = Vehicle(101, "toyota", 50)
car2 = Vehicle(102, "honda", 45)

print("Car 1 Details:")
car1.display_details()
print("Rent for 5 days:", car1.calculate_rent(5))

print()

print("Car 2 Details:")
car2.display_details()
print("Rent for 3 days:", car2.calculate_rent(3))
