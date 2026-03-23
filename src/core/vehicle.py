class Vehicle:
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage

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