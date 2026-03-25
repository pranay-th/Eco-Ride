import json
from ..schemas.electric_car import ElectricCar
from ..schemas.electric_scooter import ElectricScooter

def save_to_json(hubs, filename):
    data = {}
    
    for hub_name, vehicles in hubs.items():
        data[hub_name] = []
        for vehicle in vehicles:
            vehicle_type = type(vehicle).__name__
            
            vehicle_data = {
                'vehicle_type': vehicle_type,
                'vehicle_id': vehicle.vehicle_id,
                'model': vehicle.model,
                'battery_percentage': vehicle.get_battery_percentage(),
                'maintenance_status': vehicle.get_maintenance_status(),
                'rental_price': vehicle.get_rental_price()
            }
            
            if isinstance(vehicle, ElectricCar):
                vehicle_data['seating_capacity'] = vehicle.seating_capacity
            else:
                vehicle_data['max_speed_limit'] = vehicle.max_speed_limit
            
            data[hub_name].append(vehicle_data)
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"Fleet data saved to {filename}")

def load_from_json(hubs, filename, add_hub_callback):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        
        for hub_name, vehicles in data.items():
            if hub_name not in hubs:
                add_hub_callback(hub_name)
            
            for vehicle_data in vehicles:
                vehicle_type = vehicle_data['vehicle_type']
                vehicle_id = vehicle_data['vehicle_id']
                model = vehicle_data['model']
                battery_percentage = vehicle_data['battery_percentage']
                maintenance_status = vehicle_data['maintenance_status']
                rental_price = vehicle_data['rental_price']
                
                if vehicle_type == 'ElectricCar':
                    seating_capacity = vehicle_data['seating_capacity']
                    vehicle = ElectricCar(vehicle_id, model, battery_percentage, seating_capacity)
                else:
                    max_speed_limit = vehicle_data['max_speed_limit']
                    vehicle = ElectricScooter(vehicle_id, model, battery_percentage, max_speed_limit)
                
                vehicle.set_maintenance_status(maintenance_status)
                vehicle.set_rental_price(rental_price)
                
                hubs[hub_name].append(vehicle)
        
        print(f"Fleet data loaded from {filename}")
    
    except FileNotFoundError:
        print(f"File {filename} not found.")
