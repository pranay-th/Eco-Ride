from .vehicle import Vehicle

class ElectricCar(Vehicle):
    def __init__(self,vehicle_id,model,battery_percentage,seating_capacity):
        super().__init__(vehicle_id,model,battery_percentage)
        if seating_capacity<=0:
            raise ValueError("Seating Capacity cannot be negative")
        else:
            self.seating_capacity = seating_capacity
    
    def calculate_trip_cost(self, distance):
        return distance * self.get_rental_price()