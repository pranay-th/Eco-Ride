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

        
