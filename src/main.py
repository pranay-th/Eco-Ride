from src.services.fleet_service import FleetManager
from src.ui.menu import print_menu
from src.ui.cli import add_vehicle_menu


def main():
    fleet = FleetManager()
    
    fleet.load_from_csv("data/fleet_data.csv")
    
    while True:
        print_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            hub_name = input("Enter Hub Name: ")
            fleet.add_hub(hub_name)
        
        elif choice == "2":
            hub_name = input("Enter Hub Name: ")
            vehicle = add_vehicle_menu(fleet)
            if vehicle:
                fleet.add_vehicle_to_hub(hub_name, vehicle)
        
        elif choice == "3":
            hub_name = input("Enter Hub Name: ")
            fleet.display_vehicles_by_hub(hub_name)
        
        elif choice == "4":
            hubs = fleet.list_all_hubs()
            print("\nAvailable Hubs:")
            for hub in hubs:
                print(f"  - {hub}")
        
        elif choice == "5":
            min_battery = int(input("Enter Minimum Battery Level: "))
            hub_name = input("Enter Hub Name (or press Enter for all hubs): ")
            if hub_name == "":
                fleet.search_by_battery_level(min_battery)
            else:
                fleet.search_by_battery_level(min_battery, hub_name)
        
        elif choice == "6":
            hub_name = input("Enter Hub Name (or press Enter for all hubs): ")
            if hub_name == "":
                fleet.display_vehicles_by_type()
            else:
                fleet.display_vehicles_by_type(hub_name)
        
        elif choice == "7":
            hub_name = input("Enter Hub Name (or press Enter for all hubs): ")
            if hub_name == "":
                fleet.display_fleet_analytics()
            else:
                fleet.display_fleet_analytics(hub_name)
        
        elif choice == "8":
            hub_name = input("Enter Hub Name: ")
            fleet.display_vehicles_sorted_by_model(hub_name)
        
        elif choice == "9":
            hub_name = input("Enter Hub Name (or press Enter for all hubs): ")
            if hub_name == "":
                fleet.display_vehicles_sorted_by_battery()
            else:
                fleet.display_vehicles_sorted_by_battery(hub_name)
        
        elif choice == "10":
            hub_name = input("Enter Hub Name (or press Enter for all hubs): ")
            if hub_name == "":
                fleet.display_vehicles_sorted_by_rentalprice()
            else:
                fleet.display_vehicles_sorted_by_rentalprice(hub_name)
        
        elif choice == "11":
            filename = input("Enter filename (default: data/fleet_data.csv): ")
            if filename == "":
                filename = "data/fleet_data.csv"
            fleet.save_to_csv(filename)
        
        elif choice == "12":
            filename = input("Enter filename (default: data/fleet_data.csv): ")
            if filename == "":
                filename = "data/fleet_data.csv"
            fleet.load_from_csv(filename)
        
        elif choice == "13":
            filename = input("Enter filename (default: data/fleet_data.json): ")
            if filename == "":
                filename = "data/fleet_data.json"
            fleet.save_to_json(filename)
        
        elif choice == "14":
            filename = input("Enter filename (default: data/fleet_data.json): ")
            if filename == "":
                filename = "data/fleet_data.json"
            fleet.load_from_json(filename)
        
        elif choice == "0":
            print("\nSaving data before exit...")
            fleet.save_to_csv("data/fleet_data.csv")
            print("Thank you for using EcoRide Urban Mobility System!")
            break
        
        else:
            print("Invalid choice! Please try again.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
