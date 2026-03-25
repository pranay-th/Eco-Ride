from ..schemas.electric_car import ElectricCar
from ..schemas.electric_scooter import ElectricScooter
from .csv_service import save_to_csv, load_from_csv
from .json_service import save_to_json, load_from_json

class FleetManager():
    def __init__(self):
        self.hubs = {}

    def add_hub(self,hub_name):
        if hub_name in self.hubs:
            print(f"Hub {hub_name} already exists.")
            return 
        self.hubs[hub_name]=[]
        print(f"Hub {hub_name} added!")

    
    def add_vehicle_to_hub(self,hub_name,vehicle):
        if hub_name not in self.hubs:
            print(f"Hub {hub_name} does not exist.")
            return
        if vehicle not in self.hubs[hub_name]:
            self.hubs[hub_name].append(vehicle)
            print(f"Vehicle {vehicle} added to Hub {hub_name} succesfully!")
        else:
            print(f"Vehicle {vehicle} already exists.")
            return

    def get_vehicles_by_hub(self,hub_name):
        if hub_name not in self.hubs:
            print(f"Hub {hub_name} does not exist.")
            return []
        return self.hubs[hub_name]

    def list_all_hubs(self):
        return list(self.hubs.keys())

    def display_vehicles_by_hub(self,hub_name):
        vehicles = self.get_vehicles_by_hub(hub_name)
        for vehicle in vehicles:
            print(vehicle)
    
    def search_by_battery_level(self,min_battery,hub_name=None):
        if hub_name:
            vehicles=self.get_vehicles_by_hub(hub_name)
        else:
            vehicles=[]
            for hub_vehicles in self.hubs.values():
                vehicles.extend(hub_vehicles)
        
        filtered_vehicles=filter(lambda v: v.get_battery_percentage() > min_battery,vehicles)

        for vehicle in filtered_vehicles:
            print(vehicle)

        
    def get_vehicles_by_type(self,hub_name=None):
        categorized={}
        if hub_name:
            vehicles=self.get_vehicles_by_hub(hub_name)
        else:
            vehicles=[]
            for hub_vehicles in self.hubs.values():
                vehicles.extend(hub_vehicles)
        
        for vehicle in vehicles:
            vehicle_type=type(vehicle).__name__
            categorized.setdefault(vehicle_type, []).append(vehicle)
        
        return categorized

    def display_vehicles_by_type(self,hub_name=None):
        categorized=self.get_vehicles_by_type(hub_name)

        for vehicle_type,vehicle_list in categorized.items():
            print(f"\n--- {vehicle_type} ---")
            for vehicle in vehicle_list:
                print(vehicle)
            print("\n")

    def get_vehicle_count_by_status(self,hub_name=None):
        categorized={}
        if hub_name:
            vehicles=self.get_vehicles_by_hub(hub_name)
        else:
            vehicles=[]
            for hub_vehicles in self.hubs.values():
                vehicles.extend(hub_vehicles)
        
        for vehicle in vehicles:
            vehicle_status=vehicle.get_maintenance_status()
            categorized[vehicle_status]=categorized.get(vehicle_status,0)+1
            
        return categorized
    
    def display_fleet_analytics(self,hub_name=None):
        status_count=self.get_vehicle_count_by_status(hub_name)
        print("=== Fleet Analytics ===")
        for status, count in status_count.items():
            print(f"{status}: {count}")

    def display_vehicles_sorted_by_model(self,hub_name):
        vehicles=self.get_vehicles_by_hub(hub_name)

        sorted_vehicles = sorted(vehicles, key=lambda v: v.model.lower())
        print(f"Here is the vehicle models in the hub sorted alphabetically")
        for vehicle in sorted_vehicles:
            print(vehicle)

    def display_vehicles_sorted_by_battery(self,hub_name=None,reverse=True):
        if hub_name:
            vehicles=self.get_vehicles_by_hub(hub_name)
        else:
            vehicles=[]
            for hub_vehicles in self.hubs.values():
                vehicles.extend(hub_vehicles)

        sorted_vehicles = sorted(vehicles, key=lambda v: v.get_battery_percentage(),reverse=True)
        print("Here are vehicles sorted by battery percentage")
        for vehicle in sorted_vehicles:
            print(vehicle)

    
    def display_vehicles_sorted_by_rentalprice(self,hub_name=None,reverse=True):
        if hub_name:
            vehicles=self.get_vehicles_by_hub(hub_name)
        else:
            vehicles=[]
            for hub_vehicles in self.hubs.values():
                vehicles.extend(hub_vehicles)
            
        sorted_vehicles = sorted(vehicles, key=lambda v: v.get_rental_price(),reverse=True)
        print("Here are vehicles sorted by rental price")
        for vehicle in sorted_vehicles:
            print(vehicle)

    def save_to_csv(self, filename):
        save_to_csv(self.hubs, filename)

    def load_from_csv(self, filename):
        load_from_csv(self.hubs, filename, self.add_hub)

    def save_to_json(self, filename):
        save_to_json(self.hubs, filename)

    def load_from_json(self, filename):
        load_from_json(self.hubs, filename, self.add_hub)
