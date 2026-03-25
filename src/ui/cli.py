from ..schemas.electric_car import ElectricCar
from ..schemas.electric_scooter import ElectricScooter


def add_vehicle_menu(fleet):
    print("\nSelect Vehicle Type:")
    print("1. Electric Car")
    print("2. Electric Scooter")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        vehicle_id = input("Enter Vehicle ID: ")
        model = input("Enter Model: ")
        battery = int(input("Enter Battery Percentage: "))
        seating = int(input("Enter Seating Capacity: "))
        
        vehicle = ElectricCar(vehicle_id, model, battery, seating)
        return vehicle
    
    elif choice == "2":
        vehicle_id = input("Enter Vehicle ID: ")
        model = input("Enter Model: ")
        battery = int(input("Enter Battery Percentage: "))
        max_speed = int(input("Enter Max Speed Limit: "))
        
        vehicle = ElectricScooter(vehicle_id, model, battery, max_speed)
        return vehicle
    
    else:
        print("Invalid choice!")
        return None
