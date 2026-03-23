from .vehicle import Vehicle

class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        if max_speed_limit<1:
            raise ValueError("Max speed cannot be negative")
        else:
            self.max_speed_limit = max_speed_limit
