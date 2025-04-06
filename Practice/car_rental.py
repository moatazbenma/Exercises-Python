class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Rented"
        return f"{self.year} {self.make} {self.model} - {status}"
    
class CarRental:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Car '{car.make} {car.model}' added to the fleet.")

    def remove_car(self, make, model):
        for car in self.cars:
            if car.make == make and car.model == model:
                self.cars.remove(car)
                print(f"Car '{car.make} {car.model}' removed from the fleet.")
                return
        print(f"No car found with make '{make}' and model '{model}'.")

    def rent_car(self, make, model):
        for car in self.cars:
            if car.make == make and car.model == model:
                if car.available:
                    car.available = False
                    print(f"Car '{make} {model}' has been rented out.")
                else:
                    print(f"Car '{make} {model}' is already rented.")
                return
        print(f"No car found with make '{make}' and model '{model}'.")

    def return_car(self, make, model):
        for car in self.cars:
            if car.make == make and car.model == model:
                if not car.available:
                    car.available = True
                    print(f"Car '{make} {model}' has been returned.")
                else:
                    print(f"Car '{make} {model}' was not rented.")
                return
        print(f"No car found with make '{make}' and model '{model}'.")

    def display_cars(self):
        print("\nCar Fleet:")
        if not self.cars:
            print("No cars available.")
        else:
            for car in self.cars:
                print(f"- {car}")
        print()


# Adding cars
car1 = Car("Toyota", "Camry", 2020)
# 🚀 Example Usage
rental = CarRental()

rental.add_car(car1)


# Displaying cars
rental.display_cars()

