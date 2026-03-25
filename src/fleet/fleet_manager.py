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
        if vehicle in self.hubs[hub_name]:
            self.hubs[hub_name].append(vehicle)
            print(f"Vehicle {vehicle} added to Hub {hub_name} succesfully!")
        else:
            print(f"Vehicle {vehicle} already exists.")

    def get_vehicles_by_hub(self,hub_name):
        if hub_name not in self.hubs:
            print(f"Hub {hub_name} does not exist.")
            return []
        return self.hubs[hub_name]

    def list_all_hubs(self):
        return list(self.hubs.keys())
