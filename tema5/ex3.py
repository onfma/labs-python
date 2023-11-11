class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, distance):
        return distance / self.fuel_efficiency

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, distance):
        return distance / self.fuel_efficiency

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return f"Towing Capacity: {self.towing_capacity} lbs"


car = Car("Toyota", "Camry", 2022, 30)
print(f"{car.display_info()} - Mileage: {car.calculate_mileage(300)} miles per gallon \n")

motorcycle = Motorcycle("Harley-Davidson", "Street Glide", 2022, 45)
print(f"{motorcycle.display_info()} - Mileage: {motorcycle.calculate_mileage(200)} miles per gallon \n")

truck = Truck("Ford", "F-150", 2022, 10000)
print(f"{truck.display_info()} - {truck.calculate_towing_capacity()}")
