class CarRegistry:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        if self.fuel_type == "Gasoline":
            self.registry = GasolineCarRegistry()
        elif self.fuel_type == "Electric":
            self.registry = ElectricCarRegistry()

    def register_car(self, make, model, year):
        car = Car(make, model, year, self.fuel_type)
        self.registry.register_car(car)

    def unregister_car(self, make, model, year):
        car = Car(make, model, year, self.fuel_type)
        self.registry.unregister_car(car)

    def list_cars(self):
        self.registry.list_cars()


class Car:
    def __init__(self, make, model, year, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.fuel_type})"


class CarRegistryInterface:
    def register_car(self, car):
        pass

    def unregister_car(self, car):
        pass

    def list_cars(self):
        pass


class CarRegistryObserver:
    def __init__(self, bridge):
        self.bridge = bridge

    def car_registered(self, car):
        pass

    def car_unregistered(self, car):
        pass


class GasolineCarRegistry(CarRegistryInterface):
    def __init__(self):
        self.cars = []
        self.observers = []

    def register_car(self, car):
        if car.fuel_type == "Gasoline":
            self.cars.append(car)
            print(f"Gasoline car {car} registered successfully.")
            self.notify_observers()
        else:
            print(f"Car {car} cannot be registered in the Gasoline registry because it is not a gasoline car.")

    def unregister_car(self, car):
        try:
            self.cars.remove(car)
            print(f"Gasoline car {car} unregistered successfully.")
            self.notify_observers()
        except ValueError:
            print(f"Gasoline car {car} is not registered in the registry.")

    def list_cars(self):
        if not self.cars:
            print("No gasoline cars registered in the registry.")
        else:
            print("Registered gasoline cars:")
            for car in self.cars:
                print(car)

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)


class ElectricCarRegistry(CarRegistryInterface):
    def __init__(self):
        self.cars = []
        self.observers = []

    def register_car(self, car):
        if car.fuel_type == "Electric":
            self.cars.append(car)
            print(f"Electric car {car} registered successfully.")
            self.notify_observers()
        else:
            print(f"Car {car} cannot be registered in the Electric registry because it is not a gasoline car.")

    def unregister_car(self, car):
        try:
            self.cars.remove(car)
            print(f"Electric car {car} unregistered successfully.")
            self.notify_observers()
        except ValueError:
            print(f"Electric car {car} is not registered in the registry.")

    def list_cars(self):
        if not self.cars:
            print("No electric cars registered in the registry.")
        else:
            print("Registered electric cars:")
            for car in self.cars:
                print(car)

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

class CarRegistryBridge:
    def __init__(self, registry):
        self.registry = registry

    def register_car(self, car):
        self.registry.register_car(car)

    def unregister_car(self, car):
        self.registry.unregister_car(car)

    def list_cars(self):
        self.registry.list_cars()

gasoline_registry = CarRegistry("Gasoline")
electric_registry = CarRegistry("Electric")

gasoline_registry.register_car("Toyota", "Camry", 2015)
gasoline_registry.register_car("Honda", "Civic", 2010)
electric_registry.register_car("Tesla", "Model S", 2020)
electric_registry.register_car("Tesla", "Model X", 2021)

gasoline_registry.list_cars()
electric_registry.list_cars()