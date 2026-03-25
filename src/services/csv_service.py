import csv
from ..schemas.electric_car import ElectricCar
from ..schemas.electric_scooter import ElectricScooter

def save_to_csv(hubs, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(['hub_name', 'vehicle_type', 'vehicle_id', 'model', 'battery_percentage', 'maintenance_status', 'rental_price', 'seating_capacity', 'max_speed_limit'])
        
        for hub_name, vehicles in hubs.items():
            for vehicle in vehicles:
                vehicle_type = type(vehicle).__name__
                
                if isinstance(vehicle, ElectricCar):
                    seating_capacity = vehicle.seating_capacity
                    max_speed_limit = ''
                else:
                    seating_capacity = ''
                    max_speed_limit = vehicle.max_speed_limit
                
                writer.writerow([
                    hub_name,
                    vehicle_type,
                    vehicle.vehicle_id,
                    vehicle.model,
                    vehicle.get_battery_percentage(),
                    vehicle.get_maintenance_status(),
                    vehicle.get_rental_price(),
                    seating_capacity,
                    max_speed_limit
                ])
        
        print(f"Fleet data saved to {filename}")

def load_from_csv(hubs, filename, add_hub_callback):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            
            for row in reader:
                hub_name = row[0]
                vehicle_type = row[1]
                vehicle_id = row[2]
                model = row[3]
                battery_percentage = int(row[4])
                maintenance_status = row[5]
                rental_price = float(row[6])
                seating_capacity = row[7]
                max_speed_limit = row[8]
                
                if vehicle_type == 'ElectricCar':
                    vehicle = ElectricCar(vehicle_id, model, battery_percentage, int(seating_capacity))
                else:
                    vehicle = ElectricScooter(vehicle_id, model, battery_percentage, int(max_speed_limit))
                
                vehicle.set_maintenance_status(maintenance_status)
                vehicle.set_rental_price(rental_price)
                
                if hub_name not in hubs:
                    add_hub_callback(hub_name)
                
                hubs[hub_name].append(vehicle)
            
            print(f"Fleet data loaded from {filename}")
    
    except FileNotFoundError:
        print(f"File {filename} not found.")
