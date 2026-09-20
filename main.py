import json

# Bring in our classes from the other files
from vehicle import Vehicle
from customer import Customer
from rental import Rental

class RentalSystem:
    def __init__(self):
        # Keep track of everything in these lists
        self.vehicles = []
        self.customers = []
        self.rentals = []
        
        # Load up any saved data right when the program starts
        self.load_data()

    # FILE HANDLING

    def save_data(self):
        # Save vehicles
        v_list = []
        for v in self.vehicles:
            v_list.append(v.to_dictionary())
        with open("vehicles.json", "w") as f:
            json.dump(v_list, f)
        
        # Save customers
        c_list = []
        for c in self.customers:
            c_list.append(c.to_dictionary())
        with open("customers.json", "w") as f:
            json.dump(c_list, f)
            
        # Save rentals
        r_list = []
        for r in self.rentals:
            r_list.append(r.to_dictionary())
        with open("rentals.json", "w") as f:
            json.dump(r_list, f)
            
        print("\nAll data has been saved to files!")

    def load_data(self):
        # Try to load vehicles. If the file doesn't exist yet, we just pass and start empty.
        try:
            with open("vehicles.json", "r") as f:
                v_data = json.load(f)
                for item in v_data:
                    # Rebuild the Vehicle object from the dictionary
                    v = Vehicle(item["vehicle_id"], item["registration"], item["make"], 
                                item["model"], item["daily_rate"], item["is_available"])
                    self.vehicles.append(v)
        except FileNotFoundError:
            pass 

        # Try to load customers
        try:
            with open("customers.json", "r") as f:
                c_data = json.load(f)
                for item in c_data:
                    c = Customer(item["customer_id"], item["customer_name"], item["phone_number"])
                    self.customers.append(c)
        except FileNotFoundError:
            pass

        # Try to load rentals
        try:
            with open("rentals.json", "r") as f:
                r_data = json.load(f)
                for item in r_data:
                    r = Rental(item["rental_id"], item["vehicle_id"], item["customer_id"], 
                               item["days"], item["total_cost"], item["is_active"])
                    self.rentals.append(r)
        except FileNotFoundError:
            pass

    def update_customer_info(self):
        print("\nUpdate Customer Info")
        c_id = input("Enter Customer ID: ").strip()
        customer = self.get_customer_by_id(c_id)

        if customer is None:
            print("Error! Customer not found.")
            return

        print("\nCurrent Customer Info:")
        customer.display_details()
        print("\nPlease leave input blank to keep current customer details.")

        new_name = input(f"Enter new name ({customer.customer_name}): ").strip() or None
        new_phone = input(f"Enter new phone number ({customer.phone_number}): ").strip() or None
        new_email = input(f"Enter new email address ({customer.email}): ").strip() or None
        new_driver_license = input(f"Enter new driver license ({customer.driver_license}): ").strip() or None

        customer.update_details(new_name, new_phone, new_email, new_driver_license)
        print("Customer details updated successfully!!")
    def update_vehicle_details(self):
        print("\nUpdate Vehicle Details")
        v_id = input("Enter Vehicle ID: ").strip()
        car = self.get_vehicle_by_id(v_id)

        if car is None:
            print("Error! Vehicle not found.")
            return

        print("\nCurrent Vehicle Details")
        print(
            f"Vehicle ID: {car.vehicle_id}\n Registration: {car.registration}\n Make: {car.make}\n Model: {car.model}\n Daily Rate: ${car.daily_rate}\n")
        print("Please leave input blank to keep current vehicle details.")

        # Reassigning variables
        new_registration = input(f"Enter new registration number ({car.registration}): ").strip() or None
        new_make = input(f"Enter new make ({car.make}): ").strip() or None
        new_model = input(f"Enter a new model ({car.model}): ").strip() or None
        new_daily_rate = input(f"Enter a new rate (${car.daily_rate}): ").strip() or None

        new_rate = None
        if new_daily_rate is not None:
            try:
                parsed_rate = float(new_daily_rate)
                if parsed_rate <= 0:
                    print("Invalid rate. Daily rate will remain unchanged.")
                else:
                    new_rate = parsed_rate
            except ValueError:
                print("Invalid number input. Rate will remain unchanged.")

        car.update_details(new_registration, new_make, new_model, new_rate)
        print("Vehicle information updated successfully!")

    # I added these to make searching easier and keep the main code clean
    def get_vehicle_by_id(self, v_id):
        for v in self.vehicles:
            if v.vehicle_id == v_id:
                return v
        return None

    def get_customer_by_id(self, c_id):
        for c in self.customers:
            if c.customer_id == c_id:
                return c
        return None


    # CORE FEATURES

    def add_vehicle(self):
        print("\n--- Add a New Vehicle ---")
        v_id = input("Enter Vehicle ID: ")
        
        # Validation: Make sure they didn't leave it blank
        if v_id == "":
            print("Oops, ID cannot be blank.")
            return
            
        # Validation: Check if this ID is already taken
        if self.get_vehicle_by_id(v_id) != None:
            print("Error: A vehicle with that ID already exists.")
            return

        reg = input("Enter Registration Number: ")
        make = input("Enter Make (e.g., Ford): ")
        model = input("Enter Model (e.g., Focus): ")
        
        # Exception Handling: Make sure the rate is actually a number
        try:
            rate = float(input("Enter Daily Rate ($): "))
            if rate <= 0:
                print("Rate must be greater than zero.")
                return
        except ValueError:
            print("That's not a valid number. Please try again.")
            return

        # Create the object and add it to our list
        new_car = Vehicle(v_id, reg, make, model, rate)
        self.vehicles.append(new_car)
        print("Vehicle added successfully!")


    def display_vehicles(self):
        print("\n--- Vehicle Fleet ---")
        if len(self.vehicles) == 0:
            print("No vehicles in the system yet.")
        else:
            for v in self.vehicles:
                v.display_details()

    def search_vehicle(self):
        print("\n--- Search for a Vehicle ---")
        search_term = input("Enter Vehicle ID or Registration: ")
        
        found = False
        for v in self.vehicles:
            if v.search_for_vehicle(search_term):
                found = True
                
        if not found:
            print("Could not find a vehicle matching that search.")

    def register_customer(self):
        print("\n--- Register a Customer ---")
        c_id = input("Enter Customer ID: ")
        
        if c_id == "":
            print("Customer ID cannot be blank.")
            return
            
        if self.get_customer_by_id(c_id) != None:
            print("Error: This Customer ID is already registered.")
            return
            
        name = input("Enter Full Name: ")
        phone = input("Enter Phone Number: ")
        
        new_cust = Customer(c_id, name, phone)
        self.customers.append(new_cust)
        print(f"Customer {name} registered successfully!")

    def display_customers(self):
        print("\n--- Customer List ---")
        if len(self.customers) == 0:
            print("No customers registered yet.")
        else:
            for c in self.customers:
                c.display_details()

    def rent_vehicle(self):
        print("\n--- Rent a Vehicle ---")
        r_id = input("Enter a Rental ID for this transaction: ")
        
        # Check for duplicate rental ID
        for r in self.rentals:
            if r.rental_id == r_id:
                print("Error: Rental ID already used.")
                return

        v_id = input("Enter Vehicle ID: ")
        car = self.get_vehicle_by_id(v_id)
        
        if car == None:
            print("Vehicle not found.")
            return
            
        # Validation: Stop double booking
        if car.is_available == False:
            print("Sorry, this car is already rented out.")
            return

        c_id = input("Enter Customer ID: ")
        cust = self.get_customer_by_id(c_id)
        
        if cust == None:
            print("Customer not found. Please register them first.")
            return

        try:
            days = int(input("How many days will they rent it? "))
            if days <= 0:
                print("Days must be at least 1.")
                return
        except ValueError:
            print("Please enter a valid whole number for days.")
            return

        # Create the rental record
        new_rental = Rental(r_id, v_id, c_id, days)
        
        # Calculate how much it will cost based on the car's daily rate
        total_cost = new_rental.calculate_cost(car.daily_rate)
        
        # Update the car's status so it can't be rented again
        #instead of assigning is_available to false, I just called the function as it is in main
        car.rent_a_vehicle()
        
        self.rentals.append(new_rental)
        print(f"Rental successful! The total cost will be ${total_cost}")

    def return_vehicle(self):
        print("\n--- Return a Vehicle ---")
        r_id = input("Enter Rental ID: ")
        
        # Look through our list to find the active rental
        rental_record = None
        for r in self.rentals:
            if r.rental_id == r_id and r.is_active == True:
                rental_record = r
                break
                
        if rental_record == None:
            print("Could not find an active rental with that ID.")
            return

        # Mark the rental as finished
        rental_record.is_active = False
        
        # Find the car and make it available for the next customer
        car = self.get_vehicle_by_id(rental_record.vehicle_id)
        if car != None:
            #calls this fuction so that it makes the car available
            car.return_a_vehicle()
            
        print(f"Vehicle returned! Customer owes: ${rental_record.total_cost}")

    def display_active_rentals(self):
        print("\n--- Active Rentals ---")
        count = 0
        for r in self.rentals:
            if r.is_active:
                r.display_details()
                count += 1
                
        if count == 0:
            print("There are no active rentals right now.")

# Main program loop

# Set up our application 
app = RentalSystem()

# Keep showing the menu until the user wants to exit
while True:
    print(" VEHICLE RENTAL SYSTEM")
    print("1. Add Vehicle")
    print("2. Display All Vehicles")
    print("3. Search for a Vehicle")
    print("4. Register Customer")
    print("5. Display Customers")
    print("6. Rent a Vehicle")
    print("7. Return a Vehicle")
    print("8. Display Active Rentals")
    print("9. Save Data")
    print("10. Update existing vehicle details")
    print("11. Update existing customer details")
    print("12. Exit")
    
    choice = input("\nEnter your choice (1-10): ")
    
    if choice == '1':
        app.add_vehicle()
    elif choice == '2':
        app.display_vehicles()
    elif choice == '3':
        app.search_vehicle()
    elif choice == '4':
        app.register_customer()
    elif choice == '5':
        app.display_customers()
    elif choice == '6':
        app.rent_vehicle()
    elif choice == '7':
        app.return_vehicle()
    elif choice == '8':
        app.display_active_rentals()
    elif choice == '9':
        app.save_data()
    elif choice == '10':
        app.update_vehicle_details()
    elif choice == '11':
        app.update_customer_info()
    elif choice == '12':
        # Always save right before closing so we don't lose our work
        app.save_data() 
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice. Please pick a number from 1 to 10.")