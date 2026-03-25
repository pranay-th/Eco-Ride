from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self,vehicle_id,model,battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model

        self.__battery_percentage = 0
        self.__maintenance_status = "Available"
        self.__rental_price = 0.0

        self.set_battery_percentage(battery_percentage)

    def get_battery_percentage(self):
        return self.__battery_percentage

    def set_battery_percentage(self,value):
        if value>100 or value<0:
            raise ValueError("Battery must be between 0 to 100")
        else:
            self.__battery_percentage=value

    def get_maintenance_status(self):
        return self.__maintenance_status

    def set_maintenance_status(self,status):
        allow = ["Available","On Trip","Under Maintenance"]
        if status in allow:
            self.__maintenance_status=status
        else:
            raise ValueError("Invalid Maintenance Status")

    def get_rental_price(self):
        return self.__rental_price

    def set_rental_price(self,price):
        if price<0:
            raise ValueError("Rental price cannot be negative.")
        else:
            self.__rental_price = price

    @abstractmethod
    def calculate_trip_cost(self,distance):
        pass
    
    def __eq__(self,other):
        if isinstance(other,Vehicle):
            return self.vehicle_id == other.vehicle_id
        else:
            return False

    def __str__(self):
        return f"{type(self).__name__} {self.vehicle_id}({self.model}) - Battery: {self.get_battery_percentage()}, Status:{self.get_maintenance_status()}."

    def main():
        print(r"""
  ______          _____  _     _      
 |  ____|        |  __ \(_)   | |     
 | |__   ___ ___ | |__) |_  __| | ___ 
 |  __| / __/ _ \|  _  /| |/ _` |/ _ \
 | |___| (_| (_) | | \ \| | (_| |  __/
 |______\___\___/|_|  \_\_|\__,_|\___|
        """)
        print("Welcome to Eco-Ride Urban Mobility System")