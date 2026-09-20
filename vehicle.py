class Vehicle:
    def __init__(self, vehicle_id=None, registration=None, make=None, model=None, daily_rate=0.0, is_available=True):
        #initializes these variables only
        self.vehicle_id = vehicle_id
        self.registration = registration
        self.make = make
        self.model = model
        self.daily_rate = float(daily_rate)
        self.is_available = is_available

#removed creating a new vehicle(within main)

    def rent_a_vehicle(self):
        self.is_available = False
        #prevent a rented vehicle from being rented

    def return_a_vehicle(self):
        self.is_available = True

    def search_for_vehicle(self, search_term):
        # Checks this vehicle's own ID and registration against the search term.
        # Returns True (and prints the details) if it's a match, False otherwise,
        # so RentalSystem.search_vehicle() can just loop over vehicles and ask each one.
        if self.vehicle_id == search_term or self.registration == search_term:
            self.display_details()
            return True
        return False

    def display_details(self):
        status = "Available" if self.is_available else "Rented"
        print(f"Vehicle ID: {self.vehicle_id} | Registration: {self.registration} | Make: {self.make} | Model: {self.model} | Daily Rate: ${self.daily_rate} | Status: {status}")

    def to_dictionary(self):
        return {
            "vehicle_id": self.vehicle_id,
            "registration": self.registration,
            "make": self.make,
            "model": self.model,
            "daily_rate": self.daily_rate,
            "is_available": self.is_available
        }

    def update_details(self,new_registration=None, new_make=None, new_model=None, new_daily_rate=None):
        if new_registration:
            self.registration = new_registration
        if new_make:
            self.make = new_make
        if new_model:
            self.model = new_model
        if new_daily_rate is not None and new_daily_rate > 0:
            self.daily_rate = float(new_daily_rate)

